from flask import Flask, render_template, request, send_file
from docx import Document
import io
import os

app = Flask(__name__)

def srt_to_docx_bytes(srt_text):
    lines = srt_text.splitlines()
    text_lines = []

    for line in lines:
        line = line.strip()
        if line.isdigit():  # bỏ số thứ tự
            continue
        if "-->" in line:  # bỏ thời gian
            continue
        if line == "":
            continue
        line = line.replace("&quot;", "")
        text_lines.append(line)

    full_text = " ".join(text_lines)
    doc = Document()
    doc.add_paragraph(full_text)

    doc_io = io.BytesIO()
    doc.save(doc_io)
    doc_io.seek(0)
    return doc_io

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "srt_file" not in request.files:
            return "No file uploaded", 400
        file = request.files["srt_file"]
        if file.filename == "":
            return "No file selected", 400

        srt_text = file.read().decode("utf-8")
        doc_io = srt_to_docx_bytes(srt_text)
        output_filename = file.filename.rsplit(".", 1)[0] + ".docx"

        return send_file(
            doc_io,
            as_attachment=True,
            download_name=output_filename,
            mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    return render_template("index.html")


if __name__ == "__main__":
    # Render.com cung cấp PORT qua biến môi trường
    port = int(os.environ.get("PORT", 5000))
    # Listen tất cả host, không bật debug
    app.run(host="0.0.0.0", port=port)
