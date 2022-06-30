from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename

import main

app = Flask(__name__)

UPLOAD_FOLDER = 'static/'

app.secret_key = os.environ.get('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    files = request.files.getlist('file')
    # if file.filename == '':
    #     flash('No image selected for uploading')
    #     return redirect(request.url)
    path = [0, 0]
    i = 0
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path[i] = (UPLOAD_FOLDER + filename)
            i += 1
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # print('upload_image filename: ' + filename)
        # flash('Image successfully uploaded and displayed below')
        # return render_template('index.html', filename=filename)

        else:
            flash('Allowed image types are - png, jpg, jpeg, gif')
            return redirect(request.url)

    ans = main.evaluate(path[0], path[1])
    answer = {
        'img1': path[0],
        'img2': path[1],
        'sementic_score': ans[0],
        'grammatical_errors': ans[1]
    }

    return render_template("index.html", your_result=answer)


@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == "__main__":
    app.run(debug=True)
