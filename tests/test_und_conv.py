import pytest
from und_fisicas import *

####################### 1. Testes de Temperatura #######################

def test_celsius_fahrenheit():
    """Testa a conversão de Celsius para Fahrenheit"""
    assert celsius_fahrenheit(0) == 32  # Ponto de congelamento da água
    assert celsius_fahrenheit(100) == 212  # Ponto de ebulição da água
    assert celsius_fahrenheit(-40) == -40  # Teste com valores negativos
    assert celsius_fahrenheit(37) == 98.6  # Temperatura corporal média

def test_fahrenheit_celsius():
    """Testa a conversão de Fahrenheit para Celsius"""
    assert fahrenheit_celsius(32) == 0  # Ponto de congelamento da água
    assert fahrenheit_celsius(212) == 100  # Ponto de ebulição da água
    assert fahrenheit_celsius(-40) == -40  # Teste com valores negativos
    assert fahrenheit_celsius(98.6) == 37  # Temperatura corporal média

def test_celsius_kelvin():
    """Testa a conversão de Celsius para Kelvin"""
    assert celsius_kelvin(0) == 273.15  # Ponto de congelamento da água
    assert celsius_kelvin(100) == 373.15  # Ponto de ebulição da água
    assert celsius_kelvin(-273.15) == 0  # Zero absoluto
    assert celsius_kelvin(37) == 310.15  # Temperatura corporal média

def test_kelvin_celsius():
    """Testa a conversão de Kelvin para Celsius"""
    assert kelvin_celsius(273.15) == 0  # Ponto de congelamento da água
    assert kelvin_celsius(373.15) == 100  # Ponto de ebulição da água
    assert kelvin_celsius(0) == -273.15  # Zero absoluto
    assert kelvin_celsius(310.15) == 37  # Temperatura corporal média

def test_fahrenheit_kelvin():
    """Testa a conversão de Fahrenheit para Kelvin"""
    assert fahrenheit_kelvin(32) == 273.15  # Ponto de congelamento da água
    assert fahrenheit_kelvin(212) == 373.15  # Ponto de ebulição da água
    assert fahrenheit_kelvin(-40) == 233.15  # Teste com valores negativos
    assert fahrenheit_kelvin(98.6) == 310.15  # Temperatura corporal média

def test_kelvin_fahrenheit():
    """Testa a conversão de Kelvin para Fahrenheit"""
    assert kelvin_fahrenheit(273.15) == 32  # Ponto de congelamento da água
    assert kelvin_fahrenheit(373.15) == 212  # Ponto de ebulição da água
    assert kelvin_fahrenheit(0) == -459.67  # Zero absoluto
    assert kelvin_fahrenheit(310.15) == 98.6  # Temperatura corporal média

####################### 2. Testes de Distância #######################

def test_metros_quilometros():
    """Testa a conversão de metros para quilômetros"""
    assert metros_quilometros(1000) == 1  # 1000 metros = 1 quilômetro
    assert metros_quilometros(5000) == 5  # 5000 metros = 5 quilômetros
    assert metros_quilometros(0) == 0  # 0 metros = 0 quilômetro
    assert metros_quilometros(1234) == 1.234  # Valor não inteiro

def test_quilometros_metros():
    """Testa a conversão de quilômetros para metros"""
    assert quilometros_metros(1) == 1000  # 1 quilômetro = 1000 metros
    assert quilometros_metros(5) == 5000  # 5 quilômetros = 5000 metros
    assert quilometros_metros(0) == 0  # 0 quilômetro = 0 metros
    assert quilometros_metros(1.234) == 1234  # Valor não inteiro

def test_milhas_quilometros():
    """Testa a conversão de milhas para quilômetros"""
    assert milhas_quilometros(1) == 1.60934  # 1 milha = 1.60934 quilômetros
    assert milhas_quilometros(5) == 8.0467  # 5 milhas = 8.0467 quilômetros
    assert milhas_quilometros(0) == 0  # 0 milhas = 0 quilômetros
    assert milhas_quilometros(0.5) == 0.80467  # Valor não inteiro

def test_quilometros_milhas():
    """Testa a conversão de quilômetros para milhas"""
    assert quilometros_milhas(1) == 0.621371  # 1 quilômetro = 0.621371 milhas
    assert quilometros_milhas(5) == 3.106855  # 5 quilômetros = 3.106855 milhas
    assert quilometros_milhas(0) == 0  # 0 quilômetros = 0 milhas
    assert quilometros_milhas(1.60934) == 1  # 1 milha = 1 quilômetro

####################### 3. Testes de Peso #######################

def test_quilos_libras():
    """Testa a conversão de quilogramas para libras"""
    assert quilos_libras(1) == 2.20462  # 1 quilograma = 2.20462 libras
    assert quilos_libras(5) == 11.0231  # 5 quilogramas = 11.0231 libras
    assert quilos_libras(0) == 0  # 0 quilograma = 0 libras
    assert quilos_libras(10.5) == 23.1495  # Valor não inteiro

def test_libras_quilos():
    """Testa a conversão de libras para quilogramas"""
    assert libras_quilos(2.20462) == 1  # 2.20462 libras = 1 quilograma
    assert libras_quilos(11.0231) == 5  # 11.0231 libras = 5 quilogramas
    assert libras_quilos(0) == 0  # 0 libras = 0 quilogramas
    assert libras_quilos(23.1495) == 10.5  # Valor não inteiro

def test_gramas_quilos():
    """Testa a conversão de gramas para quilogramas"""
    assert gramas_quilos(1000) == 1  # 1000 gramas = 1 quilograma
    assert gramas_quilos(5000) == 5  # 5000 gramas = 5 quilogramas
    assert gramas_quilos(0) == 0  # 0 gramas = 0 quilogramas
    assert gramas_quilos(234) == 0.234  # Valor não inteiro

def test_quilos_gramas():
    """Testa a conversão de quilogramas para gramas"""
    assert quilos_gramas(1) == 1000  # 1 quilograma = 1000 gramas
    assert quilos_gramas(5) == 5000  # 5 quilogramas = 5000 gramas
    assert quilos_gramas(0) == 0  # 0 quilograma = 0 gramas
    assert quilos_gramas(10.5) == 10500  # Valor não inteiro

####################### 4. Testes de Tempo #######################

def test_segundos_para_minutos():
    """Testa a conversão de segundos para minutos"""
    assert segundos_para_minutos(60) == 1  # 60 segundos = 1 minuto
    assert segundos_para_minutos(120) == 2  # 120 segundos = 2 minutos
    assert segundos_para_minutos(0) == 0  # 0 segundos = 0 minutos
    assert segundos_para_minutos(150) == 2.5  # Valor não inteiro

def test_minutos_para_segundos():
    """Testa a conversão de minutos para segundos"""
    assert minutos_para_segundos(1) == 60  # 1 minuto = 60 segundos
    assert minutos_para_segundos(2) == 120  # 2 minutos = 120 segundos
    assert minutos_para_segundos(0) == 0  # 0 minutos = 0 segundos
    assert minutos_para_segundos(2.5) == 150  # Valor não inteiro

def test_horas_para_minutos():
    """Testa a conversão de horas para minutos"""
    assert horas_para_minutos(1) == 60  # 1 hora = 60 minutos
    assert horas_para_minutos(2) == 120  # 2 horas = 120 minutos
    assert horas_para_minutos(0) == 0  # 0 horas = 0 minutos
    assert horas_para_minutos(1.5) == 90  # Valor não inteiro

def test_minutos_para_horas():
    """Testa a conversão de minutos para horas"""
    assert minutos_para_horas(60) == 1  # 60 minutos = 1 hora
    assert minutos_para_horas(120) == 2  # 120 minutos = 2 horas
    assert minutos_para_horas(0) == 0  # 0 minutos = 0 horas
    assert minutos_para_horas(90) == 1.5  # Valor não inteiro

####################### 5. Testes de Velocidade #######################

def test_mps_mph():
    """Testa a conversão de metros por segundo para milhas por hora"""
    assert mps_mph(1) == 2.23694  # 1 metro por segundo = 2.23694 milhas por hora
    assert mps_mph(5) == 11.1847  # 5 metros por segundo = 11.1847 milhas por hora
    assert mps_mph(0) == 0  # 0 metros por segundo = 0 milhas por hora
    assert mps_mph(10.5) == 23.47437  # Valor não inteiro

def test_mph_mps():
    """Testa a conversão de milhas por hora para metros por segundo"""
    assert mph_mps(2.23694) == 1  # 2.23694 milhas por hora = 1 metro por segundo
    assert mph_mps(11.1847) == 5  # 11.1847 milhas por hora = 5 metros por segundo
    assert mph_mps(0) == 0  # 0 milhas por hora = 0 metros por segundo
    assert mph_mps(23.47437) == 10.5  # Valor não inteiro

def test_kph_mps():
    """Testa a conversão de quilômetros por hora para metros por segundo"""
    assert kph_mps(1) == 0.277778  # 1 quilômetro por hora = 0.277778 metros por segundo
    assert kph_mps(5) == 1.38889  # 5 quilômetros por hora = 1.38889 metros por segundo
    assert kph_mps(0) == 0  # 0 quilômetros por hora = 0 metros por segundo
    assert kph_mps(10.5) == 2.91667  # Valor não inteiro

def test_mps_kph():
    """Testa a conversão de metros por segundo para quilômetros por hora"""
    assert mps_kph(1) == 3.6  # 1 metro por segundo = 3.6 quilômetros por hora
    assert mps_kph(5) == 18  # 5 metros por segundo = 18 quilômetros por hora
    assert mps_kph(0) == 0  # 0 metros por segundo = 0 quilômetros por hora
    assert mps_kph(10.5) == 37.8  # Valor não inteiro

def test_kph_mph():
    """Testa a conversão de quilômetros por hora para milhas por hora"""
    assert kph_mph(1) == 0.621371  # 1 quilômetro por hora = 0.621371 milhas por hora
    assert kph_mph(5) == 3.106855  # 5 quilômetros por hora = 3.106855 milhas por hora
    assert kph_mph(0) == 0  # 0 quilômetros por hora = 0 milhas por hora
    assert kph_mph(10.5) == 6.5244  # Valor não inteiro

def test_mph_kph():
    """Testa a conversão de milhas por hora para quilômetros por hora"""
    assert mph_kph(1) == 1.60934  # 1 milha por hora = 1.60934 quilômetros por hora
    assert mph_kph(5) == 8.0467  # 5 milhas por hora = 8.0467 quilômetros por hora
    assert mph_kph(0) == 0  # 0 milhas por hora = 0 quilômetros por hora
    assert mph_kph(10.5) == 16.8989  # Valor não inteiro
