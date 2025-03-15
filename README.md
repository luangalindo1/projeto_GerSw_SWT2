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

# Como rodar

### Pré-Requisitos
- Python 3.10 ou mais recente instalado;
- Chave própria da [exchangerate-api](https://www.exchangerate-api.com/);
- Caso esteja executando em Windows 10 ou 11, algum X Server, como o [VcXsrv](https://vcxsrv.com/).

### Instruções Gerais
1. Clone este repositório: `git clone https://github.com/luangalindo1/projeto_GerSw_SWT2`
2. Crie no diretório do repositório um arquivo `.env` e coloque sua chave da exchangerate-api, seguindo a seguinte sintaxe: API_KEY="[YOUR-API-KEY]"
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute o código: `python conversor.py`

## Instruções do Dockerfile
1. No diretório, construa a imagem Docker: `docker build -t img_conversor .`
2. Verifique se a imagem foi criada: `docker images`
3. Rode o contêiner: `docker run -e DISPLAY=host.docker.internal:0 --name conteiner_conversor -d img_conversor`
    1. Se estiver no Windows, tenha certeza que está no powershell e previamente tenha inserido o comando `$env:DISPLAY="host.docker.internal:0"`
4. Verifique os logs do contêiner: `docker logs conteiner_conversor`
5. Execute o contêiner para interagir: `docker exec -it conteiner_conversor bash`
6. Pare a execução quando desejar: `docker stop conteiner_conversor`
7. Remova o contêiner (opcional): `docker rm conteiner_conversor`

### Atenção!
- Por conta da necessidade de interface gráfica, não é recomendável a utilização do Docker Desktop para execução deste software. É necessário utilizar linha de comando para que um display adequado possa ser configurado. 

## Link para a Imagem do Container no Docker Hub:
- https://hub.docker.com/repository/docker/pcgomesp/conversor-tk-gui/general

## Exemplo de execução com Docker e VcXsrv no Windows 10:
No powershell, tendo feito o Git clone posto acima, criado seu próprio arquivo .env e estando com ambos Python e Dockers instalados, insira os seguintes comandos:

1. $env:DISPLAY="host.docker.internal:0"
2. docker build -t conversor-tk-gui .
3. docker run --rm -it -e DISPLAY=host.docker.internal:0 conversor-tk-gui

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Sinta-se à vontade para utilizar, modificar e distribuir este código conforme necessário. Para mais informações ou contribuições, por favor, entre em contato.

