import pytest
from pytest import approx
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
    assert fahrenheit_kelvin(32) == approx(273.15, rel=1e-3)  # Ponto de congelamento da água
    assert fahrenheit_kelvin(212) == approx(373.15, rel=1e-3)  # Ponto de ebulição da água
    assert fahrenheit_kelvin(-40) == approx(233.15, rel=1e-3)  # Teste com valores negativos
    assert fahrenheit_kelvin(98.6) == approx(310.15, rel=1e-3)  # Temperatura corporal média

def test_kelvin_fahrenheit():
    """Testa a conversão de Kelvin para Fahrenheit"""
    assert kelvin_fahrenheit(273.15) == approx(32, rel=1e-3)  # Ponto de congelamento da água
    assert kelvin_fahrenheit(373.15) == approx(212, rel=1e-3)  # Ponto de ebulição da água
    assert kelvin_fahrenheit(0) == approx(-459.67, rel=1e-3)  # Zero absoluto
    assert kelvin_fahrenheit(310.15) == approx(98.6, rel=1e-3)  # Temperatura corporal média

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
    assert milhas_quilometros(1) == approx(1.60934, rel=1e-3)  # 1 milha = 1.60934 quilômetros
    assert milhas_quilometros(5) == approx(8.0467, rel=1e-3)  # 5 milhas = 8.0467 quilômetros
    assert milhas_quilometros(0) == 0  # 0 milhas = 0 quilômetros
    assert milhas_quilometros(0.5) == approx(0.80467, rel=1e-3)  # Valor não inteiro

def test_quilometros_milhas():
    """Testa a conversão de quilômetros para milhas"""
    assert quilometros_milhas(1) == approx(0.621371, rel=1e-3)  # 1 quilômetro = 0.621371 milhas
    assert quilometros_milhas(5) == approx(3.106855, rel=1e-3)  # 5 quilômetros = 3.106855 milhas
    assert quilometros_milhas(0) == 0  # 0 quilômetros = 0 milhas
    assert quilometros_milhas(1.60934) == 1  # 1 milha = 1 quilômetro

####################### 3. Testes de Peso #######################

def test_quilos_libras():
    """Testa a conversão de quilogramas para libras"""
    assert quilos_libras(1) == approx(2.20462, rel=1e-3)  # 1 quilograma = 2.20462 libras
    assert quilos_libras(5) == approx(11.0231, rel=1e-3)  # 5 quilogramas = 11.0231 libras
    assert quilos_libras(0) == 0  # 0 quilograma = 0 libras
    assert quilos_libras(10.5) == approx(23.1495, rel=1e-3)  # Valor não inteiro

def test_libras_quilos():
    """Testa a conversão de libras para quilogramas"""
    assert libras_quilos(2.20462) == approx(1, rel=1e-3)  # 2.20462 libras = 1 quilograma
    assert libras_quilos(11.0231) == approx(5, rel=1e-3)  # 11.0231 libras = 5 quilogramas
    assert libras_quilos(0) == 0  # 0 libras = 0 quilogramas
    assert libras_quilos(23.1495) == approx(10.5, rel=1e-3)  # Valor não inteiro

def test_gramas_quilos():
    """Testa a conversão de gramas para quilogramas"""
    assert gramas_quilos(1000) == 1  # 1000 gramas = 1 quilograma
    assert gramas_quilos(5000) == 5  # 5000 gramas = 5 quilogramas
    assert gramas_quilos(0) == 0  # 0 gramas = 0 quilogramas
    assert gramas_quilos(234) == approx(0.234, rel=1e-3)  # Valor não inteiro

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
    assert mps_mph(1) == approx(2.23694, rel=1e-3)  # 1 m/s = 2.23694 mph
    assert mps_mph(5) == approx(11.1847, rel=1e-3)  # 5 m/s = 11.1847 mph
    assert mps_mph(0) == 0  # 0 m/s = 0 mph
    assert mps_mph(10.5) == approx(23.47437, rel=1e-3)  # Valor não inteiro

def test_mph_mps():
    """Testa a conversão de milhas por hora para metros por segundo"""
    assert mph_mps(2.23694) == approx(1, rel=1e-3)  # 2.23694 mph = 1 m/s
    assert mph_mps(11.1847) == approx(5, rel=1e-3)  # 11.1847 mph = 5 m/s
    assert mph_mps(0) == 0  # 0 mph = 0 m/s

def test_kph_mps():
    """Testa a conversão de quilômetros por hora para metros por segundo"""
    assert kph_mps(1) == approx(0.277778, rel=1e-3)  # 1 km/h = 0.277778 m/s
    assert kph_mps(5) == approx(1.38889, rel=1e-3)  # 5 km/h = 1.38889 m/s
    assert kph_mps(0) == 0  # 0 km/h = 0 m/s
    assert kph_mps(10.5) == approx(2.91667, rel=1e-3)  # Valor não inteiro

def test_mps_kph():
    """Testa a conversão de metros por segundo para quilômetros por hora"""
    assert mps_kph(1) == 3.6  # 1 m/s = 3.6 km/h
    assert mps_kph(5) == 18  # 5 m/s = 18 km/h
    assert mps_kph(0) == 0  # 0 m/s = 0 km/h
    assert mps_kph(10.5) == approx(37.8, rel=1e-3)  # Valor não inteiro

def test_kph_mph():
    """Testa a conversão de quilômetros por hora para milhas por hora"""
    assert kph_mph(1) == approx(0.621371, rel=1e-3)  # 1 km/h = 0.621371 mph
    assert kph_mph(5) == approx(3.106855, rel=1e-3)  # 5 km/h = 3.106855 mph
    assert kph_mph(0) == 0  # 0 km/h = 0 mph
    assert kph_mph(10.5) == approx(6.5244, rel=1e-3)  # Valor não inteiro

def test_mph_kph():
    """Testa a conversão de milhas por hora para quilômetros por hora"""
    assert mph_kph(1) == approx(1.60934, rel=1e-3)  # 1 mph = 1.60934 km/h
    assert mph_kph(5) == approx(8.0467, rel=1e-3)  # 5 mph = 8.0467 km/h
    assert mph_kph(0) == 0  # 0 mph = 0 km/h
    assert mph_kph(10.5) == approx(16.8989, rel=1e-3)  # Valor não inteiro
