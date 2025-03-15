# Projeto - Conversor de Unidades, Moedas e Leitor de QR Code

Este é um projeto simples de um conversor de unidades, um conversor cambial e um leitor de código QR, desenvolvido em Python. O objetivo é aplicar de forma integrada os conceitos, práticas e ferramentas de Gerência de Configuração de Software (SCM) no desenvolvimento de uma aplicação simples. Para mais detalhes, ver `projeto_enunciado.md` e `RELATÓRIO.md`.

## Autores:

Luan Fábio Marinho Galindo (luangalindo1)

Paulo César Pereira Gomes (pcgomesp)

Victor Augusto Medeiros Balbino (victorltd)

# Parte 1: Conversor de Unidades Físicas

Este projeto contém funções para a conversão de diversas unidades físicas, abrangendo categorias como temperatura, distância, peso, tempo e velocidade. As funções fornecem conversões diretas entre unidades, permitindo que você converta facilmente valores de uma unidade para outra.

## Tabelas de Conversão Implementadas

### 1. **Temperatura**
As funções a seguir realizam conversões entre diferentes escalas de temperatura:

- **`celsius_fahrenheit(celsius)`**: Converte graus Celsius para Fahrenheit.
- **`fahrenheit_celsius(fahrenheit)`**: Converte Fahrenheit para Celsius.
- **`celsius_kelvin(celsius)`**: Converte Celsius para Kelvin.
- **`kelvin_celsius(kelvin)`**: Converte Kelvin para Celsius.
- **`fahrenheit_kelvin(fahrenheit)`**: Converte Fahrenheit para Kelvin.
- **`kelvin_fahrenheit(kelvin)`**: Converte Kelvin para Fahrenheit.

### 2. **Distância**
Funções para conversão de unidades de distância:

- **`metros_quilometros(metros)`**: Converte metros para quilômetros.
- **`quilometros_metros(quilometros)`**: Converte quilômetros para metros.
- **`milhas_quilometros(milhas)`**: Converte milhas para quilômetros.
- **`quilometros_milhas(quilometros)`**: Converte quilômetros para milhas.

### 3. **Peso**
Funções para conversão de unidades de peso:

- **`quilos_libras(kg)`**: Converte quilogramas para libras.
- **`libras_quilos(libras)`**: Converte libras para quilogramas.
- **`gramas_quilos(gramas)`**: Converte gramas para quilogramas.
- **`quilos_gramas(kg)`**: Converte quilogramas para gramas.

### 4. **Tempo**
Funções para conversão de unidades de tempo:

- **`segundos_para_minutos(segundos)`**: Converte segundos para minutos.
- **`minutos_para_segundos(minutos)`**: Converte minutos para segundos.
- **`horas_para_minutos(horas)`**: Converte horas para minutos.
- **`minutos_para_horas(minutos)`**: Converte minutos para horas.

### 5. **Velocidade**
Funções para conversão de unidades de velocidade:

- **`mps_mph(mps)`**: Converte metros por segundo para milhas por hora.
- **`mph_mps(mph)`**: Converte milhas por hora para metros por segundo.
- **`kph_mps(kph)`**: Converte quilômetros por hora para metros por segundo.
- **`mps_kph(mps)`**: Converte metros por segundo para quilômetros por hora.
- **`kph_mph(kph)`**: Converte quilômetros por hora para milhas por hora.
- **`mph_kph(mph)`**: Converte milhas por hora para quilômetros por hora.

# Parte 2: Conversor de Moedas

Este projeto também contém um conversor de moedas que utiliza uma API para obter as taxas de câmbio atualizadas. As funções fornecem conversões diretas entre diferentes moedas, permitindo que você converta facilmente valores de uma moeda para outra. Para obter as taxas de câmbio atualizadas, este projeto utiliza a API da ExchangeRate-API. A chave da API é armazenada em um arquivo .env para garantir a segurança e evitar a exposição da chave no código-fonte, e deve ser copiado para mesma pasta raiz deste projeto.

### 1. **Conversões Disponíveis**
As seguintes conversões de moedas estão disponíveis:

- **`1. BRL para USD`**: Real Brasileiro para Dólar Americano
- **`2. USD para BRL`**: Dólar Americano para Real Brasileiro
- **`3. USD para EUR`**: Dólar Americano para Euro
- **`4. EUR para USD`**: Euro para Dólar Americano
- **`5. BRL para EUR`**: Real Brasileiro para Euro
- **`6. EUR para BRL`**: Euro para Real Brasileiro


# Parte 3: Leitor de QR Code

## Como rodar
1. Clone este repositório: `git clone https://github.com/luangalindo1/projeto_GerSw_SWT2`
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o código: `python conversor.py`

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Sinta-se à vontade para utilizar, modificar e distribuir este código conforme necessário. Para mais informações ou contribuições, por favor, entre em contato.

