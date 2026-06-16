import os
import time
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
ALLOWED_EXTENSIONS = {'doc', 'docx', 'pdf', 'zip', 'rar', 'py', 'txt', 'jpg', 'png', 'xlsx', 'pptx'}
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20MB

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    name = request.form.get('name', '').strip()
    file = request.files.get('file')

    if not name:
        flash('请填写姓名', 'error')
        return redirect(url_for('index'))

    if not file or file.filename == '':
        flash('请选择文件', 'error')
        return redirect(url_for('index'))

    if not allowed_file(file.filename):
        flash('不支持的文件类型', 'error')
        return redirect(url_for('index'))

    # 重命名：姓名_时间戳_原文件名
    ext = file.filename.rsplit('.', 1)[1].lower()
    timestamp = int(time.time())
    new_name = f'{name}_{timestamp}_{secure_filename(file.filename)}'
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], new_name)
    file.save(save_path)

    flash(f'{name}，上传成功 ✅', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
