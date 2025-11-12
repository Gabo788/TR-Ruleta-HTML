import random

# Definim variables per als números i colors
numeros = list(range(37))  # 0 al 36
vermells = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
negres = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
verd = [0]

# Funció per girar la ruleta (amb les 9 primeres tirades a vermell)
def girar_ruleta(numero_tirada):
    if numero_tirada <= 9:
        # Les 9 primeres tirades sempre vermell
        numero_guanyador = random.choice(vermells)
        color = "vermell"
    else:
        # Després, ruleta normal
        numero_guanyador = random.choice(numeros)
        if numero_guanyador in vermells:
            color = "vermell"
        elif numero_guanyador in negres:
            color = "negre"
        else:
            color = "verd"

    return numero_guanyador, color

# Funció per processar apostes
def apostar(tipus_aposta, valor_aposta, numero_tirada):
    numero, color = girar_ruleta(numero_tirada)
    guany = 0

    if tipus_aposta == "numero" and valor_aposta == numero:
        guany = 36  # Paga x36
    elif tipus_aposta == "color":
        if (valor_aposta == "vermell" and color == "vermell") or (valor_aposta == "negre" and color == "negre"):
            guany = 2  # Paga x2

    return numero, color, guany
