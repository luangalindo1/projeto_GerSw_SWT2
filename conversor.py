# importando os arquivos
import und_fisicas as uf
import currency_converter as cc
import qrcode_converter as qrc

# importando as bibliotecas de interface gráfica
import tkinter as tk
from tkinter import ttk

# Função para processar a conversão com base na escolha do usuário
def realizar_conversao():
    valor = float(entry_value.get())
    tipo_conversao = combo_conversao.get()

    # Dicionário com as conversões mapeadas
    conversoes = {
        "°C para °F": uf.celsius_fahrenheit,
        "°F para °C": uf.fahrenheit_celsius,
        "°C para K": uf.celsius_kelvin,
        "K para °C": uf.kelvin_celsius,
        "°F para K": uf.fahrenheit_kelvin,
        "K para °F": uf.kelvin_fahrenheit,
        "m para km": uf.metros_quilometros,
        "km para m": uf.quilometros_metros,
        "mi para km": uf.milhas_quilometros,
        "km para mi": uf.quilometros_milhas,
        "kg para lb": uf.quilos_libras,
        "lb para kg": uf.libras_quilos,
        "g para kg": uf.gramas_quilos,
        "kg para g": uf.quilos_gramas,
        "s para min": uf.segundos_para_minutos,
        "min para s": uf.minutos_para_segundos,
        "h para min": uf.horas_para_minutos,
        "min para h": uf.minutos_para_horas,
        "m/s para mi/h": uf.mps_mph,
        "mi/h para m/s": uf.mph_mps,
        "km/h para m/s": uf.kph_mps,
        "m/s para km/h": uf.mps_kph,
        "km/h para mi/h": uf.kph_mph,
        "mi/h para km/h": uf.mph_kph
    }

    try:
        # Buscar a função correta no dicionário e chamar
        funcao_conversao = conversoes[tipo_conversao]
        resultado = funcao_conversao(valor)

        # Exibir o resultado
        label_resultado.config(text=f"Resultado: {resultado:.2f}")
    except KeyError:
        label_resultado.config(text="Tipo de conversão inválido!")
    except Exception as e:
        label_resultado.config(text="Erro na conversão!")

# Função para gerar QR Code
def generate_new_qr(): 
    new_msg = entry_msg_qr.get()
    new_path = entry_save_path_qr.get()
    
    if(new_msg == ""):
        label_qr_conversion.config(text="Insira um link ou mensagem para gerar um QR Code válido")
    elif(new_path == ""):
        new_path = "my_qrcode.png"
        qrc.generate_qr_image(new_msg, new_path)
        label_qr_conversion.config(text=f"QR Code gerado em {new_path}")
    else:
        new_path = new_path + ".png"
        qrc.generate_qr_image(new_msg, new_path)
        label_qr_conversion.config(text=f"QR Code gerado em {new_path}")

# Conexão da interface com a função de ler QR Code
def read_qr(): 
    qrcode_path = entry_saved_path_qr.get()

    if qrcode_path == "":
        label_qr_read.config(text="Insira um endereço válido")
    else:
        out_msg = qrc.read_qr_image(qrcode_path)
        if out_msg == None:
            label_qr_read.config(text="Arquivo inválido")
        else:
            label_qr_read.config(text=out_msg)

# Copia texto para a área de transferência
def copy_text(): 
    texto = label_qr_read.cget("text")  
    root.clipboard_clear()              
    root.clipboard_append(texto)       
    root.update()                       

# Configuração da interface
root = tk.Tk()
root.title("Conversor de unidades, Moedas e QR Code")
root.geometry("500x500")

# Definição de páginas para cada tipo de conversão
customNotebook = ttk.Notebook(root)
frame_units = ttk.Frame(customNotebook)
frame_qrcode = ttk.Frame(customNotebook)
customNotebook.add(frame_units, text="Conversão")
customNotebook.add(frame_qrcode, text="QR Code")
customNotebook.pack(expand=True, fill="both")

# Label de título
label_titulo = tk.Label(frame_units, text="Escolha a conversão e insira o valor", font=("Arial", 14))
label_titulo.pack(pady=10)

# -> GUI da aba de conversões físicas <-
# Entrada para valor
label_value = tk.Label(frame_units, text="Valor:")
label_value.pack(pady=5)

entry_value = tk.Entry(frame_units)
entry_value.pack(pady=5)

# Combobox para selecionar a conversão
label_conversao = tk.Label(frame_units, text="Tipo de Conversão:",width=30)
label_conversao.pack(pady=5)

tipos_de_conversao = [
    "°C para °F", "°F para °C", "°C para K", "K para °C",
    "°F para K", "K para °F", "m para km", "km para m", "mi para km",
    "km para mi", "kg para lb", "lb para kg", "g para kg", "kg para g",
    "s para min", "min para s", "h para min", "min para h",
    "m/s para mi/h", "mi/h para m/s", "km/h para m/s", "m/s para km/h",
    "km/h para mi/h", "mi/h para km/h"
]


combo_conversao = ttk.Combobox(frame_units, values=tipos_de_conversao, state="readonly", justify="center")
combo_conversao.pack(pady=5)

# Botão para realizar a conversão
botao_convert = tk.Button(frame_units, text="Converter", command=realizar_conversao)
botao_convert.pack(pady=20)

# Label para exibir o resultado
label_resultado = tk.Label(frame_units, text="Resultado: ", font=("Arial", 12))
label_resultado.pack(pady=10)

# -> GUI da aba QR Code <-
label_qr_titulo = tk.Label(frame_qrcode, text="Gerador e leitor de QR Code", font=("Arial", 14))
label_qr_titulo.pack(pady=10)

# Entrada da função de transformação em QR Code
label_value_qr_msg = tk.Label(frame_qrcode, text="Mensagem ou Link:")
label_value_qr_msg.pack(pady=5)
entry_msg_qr = tk.Entry(frame_qrcode)
entry_msg_qr.pack(pady=5)
label_qr_in_path = tk.Label(frame_qrcode, text="Nome do arquivo:")
label_qr_in_path.pack(pady=5)
entry_save_path_qr = tk.Entry(frame_qrcode)
entry_save_path_qr.pack(pady=5)

# Botão e saída da transformação em QR Code
botao_qr_generate = tk.Button(frame_qrcode, text="Gerar QR Code", command=generate_new_qr)
botao_qr_generate.pack()
label_qr_conversion = tk.Label(frame_qrcode, text="")
label_qr_conversion.pack()

# Entrada da função de conversão de QR Code em Texto
label_qr_out_path = tk.Label(frame_qrcode, text="Local do arquivo no PC:")
label_qr_out_path.pack(pady=10)
entry_saved_path_qr = tk.Entry(frame_qrcode)
entry_saved_path_qr.pack(pady=5)

# Botão e saída da transformação em QR Code
botao_qr_generate = tk.Button(frame_qrcode, text="Ler QR Code", command=read_qr)
botao_qr_generate.pack()
label_qr_read = tk.Label(frame_qrcode, text="")
label_qr_read.pack()

button_copy_qr = tk.Button(frame_qrcode, text="Copiar", command=copy_text)
button_copy_qr.pack()

# -> GUI da aba de Conversão de Moedas <-

# Inicia a interface
root.mainloop()
