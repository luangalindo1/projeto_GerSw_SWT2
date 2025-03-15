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


# Parte 3: Leitor de QR Code

## Como rodar
1. Clone este repositório: `git clone https://github.com/luangalindo1/projeto_GerSw_SWT2`
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o código: `python conversor.py`

## Instruções do Dockerfile
1. No diretório, construa a imagem Docker: `docker build -t img_conversor .`
2. Verifique se a imagem foi criada: `docker images`
3. Rode o contêiner: `docker run -e DISPLAY=host.docker.internal:0 --name conteiner_conversor -d img_conversor` (**RESOLVER DISPLAY**)
4. Verifique os logs do contêiner: `docker logs conteiner_conversor`
5. Execute o contêiner para interagir: `docker exec -it conteiner_conversor bash`
6. Pare a execução quando desejar: `docker stop conteiner_conversor`
7. Remova o contêiner (opcional): `docker rm conteiner_conversor`

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Sinta-se à vontade para utilizar, modificar e distribuir este código conforme necessário. Para mais informações ou contribuições, por favor, entre em contato.

