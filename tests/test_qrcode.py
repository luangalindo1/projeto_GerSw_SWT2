import os
import pytest
import qrcode_converter

@pytest.fixture
def sample_qr(): # Func Sample -> Gera QR Code temporário para o teste abaixo
    file_name = "test_qr.png"
    qrcode_converter.generate_qr_image("https://example.com", file_name)
    yield file_name
    os.remove(file_name)

def test_read_qr_image(sample_qr):
    content = qrcode_converter.read_qr_image(sample_qr)
    assert content == "https://example.com"

def test_generate_qr_image():
    file_message = "Hello QR!"
    file_name = "test_output.png"
    qrcode_converter.generate_qr_image(file_message, file_name)
    result = qrcode_converter.read_qr_image(file_name)
    assert os.path.exists(file_name)
    assert result == file_message
    os.remove(file_name)

def test_read_qr_invalid():
    assert qrcode_converter.read_qr_image("non_existent_file.png") is None