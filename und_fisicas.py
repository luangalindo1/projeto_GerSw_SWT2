# Arquivo de desenvolvimento das funções de conversão de unidades físicas

####################### 1. Temperatura #######################

def celsius_fahrenheit(celsius):
    """Conversão de Celsius para Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_celsius(fahrenheit):
    """Conversão de Fahrenheit para Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_kelvin(celsius):
    """Conversão de Celsius para Kelvin"""
    return celsius + 273.15

def kelvin_celsius(kelvin):
    """Conversão de Kelvin para Celsius"""
    return kelvin - 273.15

def fahrenheit_kelvin(fahrenheit):
    """Conversão de Fahrenheit para Kelvin"""
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_fahrenheit(kelvin):
    """Conversão de Kelvin para Fahrenheit"""
    return (kelvin - 273.15) * 9/5 + 32

####################### 2. Distância #######################

def metros_quilometros(metros):
    """Conversão de metros para quilômetros"""
    return metros / 1000

def quilometros_metros(quilometros):
    """Conversão de quilômetros para metros"""
    return quilometros * 1000

def milhas_quilometros(milhas):
    """Conversão de milhas para quilômetros"""
    return milhas * 1.60934

def quilometros_milhas(quilometros):
    """Conversão de quilômetros para milhas"""
    return quilometros / 1.60934

####################### 3. Peso #######################

def quilos_libras(kg):
    """Conversão de quilogramas para libras"""
    return kg * 2.20462

def libras_quilos(libras):
    """Conversão de libras para quilogramas"""
    return libras / 2.20462

def gramas_quilos(gramas):
    """Conversão de gramas para quilogramas"""
    return gramas / 1000

def quilos_gramas(kg):
    """Conversão de quilogramas para gramas"""
    return kg * 1000

####################### 4. Tempo #######################

def segundos_para_minutos(segundos):
    """Conversão de segundos para minutos"""
    return segundos / 60

def minutos_para_segundos(minutos):
    """Conversão de minutos para segundos"""
    return minutos * 60

def horas_para_minutos(horas):
    """Conversão de horas para minutos"""
    return horas * 60

def minutos_para_horas(minutos):
    """Conversão de minutos para horas"""
    return minutos / 60
