import qrcode
from qrcode.constants import ERROR_CORRECT_M
from io import BytesIO
import base64

def generate_qr_base64(data: str, box_size: int = 10, border: int = 4,
                       fill_color: str = "black", back_color: str = "white") -> str:
    """
    Генерирует QR-код и возвращает его в виде строки Base64,
    готовой для встраивания в атрибут src тега img.
    """
    if not data:
        raise ValueError("Пустая строка для кодирования")

    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Сохраняем изображение в буфер в памяти
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    # Кодируем в Base64
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{img_base64}"