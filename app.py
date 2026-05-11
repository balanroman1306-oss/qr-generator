from flask import Flask, render_template, request, jsonify
from qr2 import generate_qr_base64  # предполагаем, что функция выше лежит в этом модуле

app = Flask(__name__)

@app.route('/')
def index():
    """Отдаёт главную HTML-страницу."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """
    Принимает POST-запрос с JSON, содержащим текст для кодирования,
    и возвращает JSON с Base64-изображением QR-кода.
    """
    try:
        data = request.json.get('text', '').strip()
        if not data:
            return jsonify({'error': 'Текст не может быть пустым'}), 400

        # Можно добавить параметры из запроса (цвет, размер) – по желанию
        qr_base64 = generate_qr_base64(data)
        return jsonify({'qr_image': qr_base64})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)