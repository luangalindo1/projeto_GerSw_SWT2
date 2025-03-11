import qrcode
import cv2
import os

def generate_qr_image(txt, out_file="my_qrcode.png"):
    """
    Gera uma imagem QR Code a partir de um link/mensagem
    txt -> link/mensagem a ser transformada
    out_file -> nome do arquivo de saída pro qrcode; caso não seja inserido, fica pelo nome padrão
    """

    new_qr = qrcode.QRCode(
        version = 3,
        box_size=20, 
        border=10, 
        error_correction=qrcode.constants.ERROR_CORRECT_H,
    )

    new_qr.add_data(txt)  # adiciona dado
    new_qr.make(fit=True) # gera qrcode

    new_img = new_qr.make_image() # transforma qr em imagem
    new_img.save(out_file)

    print(f"QR Code salvo como {out_file}")

def read_qr_image(file_name):
    """
    Lê uma imagem QRCode e retorna o conteúdo dele.
    file_name (str) -> Arquivo, em image, que contém o QR Code.
    """
    if not os.path.isfile(file_name):
        print("Erro: O arquivo não existe.")
        return None

    new_img = cv2.imread(file_name)

    if new_img is None:
        print("Erro: O arquivo não é uma imagem válida.")
        return None

    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(new_img)

    if data:
        print(f"Conteúdo do QR Code: {data}")
        return data
    
    else:
        print("Nenhum QR Code detectado.")
        return None