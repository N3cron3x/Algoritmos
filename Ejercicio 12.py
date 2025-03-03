# Calcular P(x) solo cuando los coeficientes (ai) son impares
# Coeficientes del polinomio (dígitos de la cédula)
coeficientes = [4, 0, 2, 3, 0, 6, 4, 3, 6, 4, 1]

# Valor de x (último dígito de la matrícula)
x = 5

# Calcular P(x) solo con coeficientes impares
resultado = sum(coef * (x ** i) for i, coef in enumerate(coeficientes) if coef % 2 != 0)

print("El valor de P(x) solo con ai impares es:", resultado)