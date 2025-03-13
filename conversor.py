# importando os arquivos
import und_fisicas as uf
import currency_converter as cc

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



# Configuração da interface
root = tk.Tk()
root.title("Conversor de Unidades Físicas")
root.geometry("400x400")

# Label de título
label_titulo = tk.Label(root, text="Escolha a conversão e insira o valor", font=("Arial", 14))
label_titulo.pack(pady=10)

# Entrada para valor
label_value = tk.Label(root, text="Valor:")
label_value.pack(pady=5)

entry_value = tk.Entry(root)
entry_value.pack(pady=5)

# Combobox para selecionar a conversão
label_conversao = tk.Label(root, text="Tipo de Conversão:",width=30)
label_conversao.pack(pady=5)

tipos_de_conversao = [
    "°C para °F", "°F para °C", "°C para K", "K para °C",
    "°F para K", "K para °F", "m para km", "km para m", "mi para km",
    "km para mi", "kg para lb", "lb para kg", "g para kg", "kg para g",
    "s para min", "min para s", "h para min", "min para h",
    "m/s para mi/h", "mi/h para m/s", "km/h para m/s", "m/s para km/h",
    "km/h para mi/h", "mi/h para km/h"
]


combo_conversao = ttk.Combobox(root, values=tipos_de_conversao, state="readonly", justify="center")
combo_conversao.pack(pady=5)

# Botão para realizar a conversão
botao_convert = tk.Button(root, text="Converter", command=realizar_conversao)
botao_convert.pack(pady=20)

# Label para exibir o resultado
label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 12))
label_resultado.pack(pady=10)

# Inicia a interface
root.mainloop()
