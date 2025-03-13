#Arquivo de desenvolvimento das funcoes de moedas


import requests
import os
from dotenv import load_dotenv

load_dotenv()

#para nao deixar a chave da api aberta para qualquer um
#foi criado um arquivo .env com a chave da api
API_KEY = os.getenv('API_KEY')

# Chave da ABASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

# Conversões pré-definidas
CONVERSOES = {
    1: ("BRL", "USD"),  # Real Brasileiro para Dólar Americano
    2: ("USD", "BRL"),  # Dólar Americano para Real Brasileiro
    3: ("USD", "EUR"),  # Dólar Americano para Euro
    4: ("EUR", "USD"),  # Euro para Dólar Americano
    5: ("BRL", "EUR"),  # Real Brasileiro para Euro
    6: ("EUR", "BRL"),  # Euro para Real Brasileiro
}

def obter_taxas_cambio():
    """
    Busca as taxas de câmbio atualizadas da API.
    """
    try:
        response = requests.get(BASE_URL)
        dados = response.json()
        if dados["result"] == "success":
            return dados["conversion_rates"]
        else:
            print("Erro ao buscar taxas de câmbio.")
            return None
    except Exception as e:
        print(f"Erro na requisição: {e}")
        return None

# Função que busca as taxas de câmbio atualizadas da API e retorna as taxas de conversão.
# Em caso de erro, imprime uma mensagem e retorna None.

def exibir_menu():
    print("Conversor de Moedas")
    print("Selecione a conversão desejada:")
    for opcao, (moeda_origem, moeda_destino) in CONVERSOES.items():
        print(f"{opcao}. {moeda_origem} para {moeda_destino}")
    print("")

# Função que exibe o menu de opções de conversão de moedas para o usuário.

def obter_opcao():
    while True:
        try:
            opcao = int(input("Digite o número da conversão desejada: "))
            if opcao in CONVERSOES:
                return opcao
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

# Função que solicita ao usuário a opção de conversão desejada e valida a entrada.
# Retorna a opção escolhida pelo usuário.

def converter_moeda(valor, moeda_origem, moeda_destino, taxas):
    taxa_origem = taxas[moeda_origem]
    taxa_destino = taxas[moeda_destino]
    valor_convertido = valor * (taxa_destino / taxa_origem)
    return valor_convertido

# Função que realiza a conversão de moeda com base nas taxas de câmbio fornecidas.
# Retorna o valor convertido.

def conversor_moedas():
    """
    Função principal que gerencia o fluxo do programa.
    """
    # Buscar taxas de câmbio
    taxas = obter_taxas_cambio()
    if not taxas:
        return  # Encerra o programa se não conseguir buscar as taxas

    exibir_menu()
    
    # Obter a conversão desejada
    opcao = obter_opcao()
    moeda_origem, moeda_destino = CONVERSOES[opcao]
    
    # Obter valor para conversão
    valor = float(input(f"Digite o valor em {moeda_origem} a ser convertido para {moeda_destino}: "))
    
    # Converter e exibir resultado
    valor_convertido = converter_moeda(valor, moeda_origem, moeda_destino, taxas)
    print(f"Valor convertido: {valor_convertido:.2f} {moeda_destino}")

# Função principal que gerencia o fluxo do programa.
# Busca as taxas de câmbio, exibe o menu, obtém a opção de conversão desejada,
# solicita o valor a ser convertido, realiza a conversão e exibe o resultado.