from flask import Flask, render_template, request, send_file
from generate import create_meme
import io

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    morning_tasks = [t for t in request.form.getlist('morning') if t.strip()]
    evening_tasks = [t for t in request.form.getlist('evening') if t.strip()]

    img_bytes = create_meme(morning_tasks, evening_tasks)

    return send_file(
        io.BytesIO(img_bytes),
        mimetype='image/jpeg',
        as_attachment=True,
        download_name='meme.jpg'
    )


if __name__ == '__main__':
    app.run(debug=True)