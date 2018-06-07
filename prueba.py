import hmencrypt as hm

# =============================================================================
# generar nuevas claves secretas (J y K) que servirán descrifrar el número
# =============================================================================
hm.generateSecretKeys()
print("Claves secretas (J, K):", hm.getSecretKeys())

# =============================================================================
# Ingreso del número N (entero) que será encriptado
# =============================================================================
N = int(input("Ingrese N: "))

# =============================================================================
# Encriptación del número N
# =============================================================================
C = hm.encrypt(N)
print("N cifrado (C):", C)
if C == N:
	print("No se realizó la encriptación")
	operador = -1
else:
	operador = 4

# =============================================================================
# Realización de las operaciones sobre C (resultado de la encriptación)
# =============================================================================
operaciones = "C"
C_ini = C
while operador > 0:
	print()
	print("Operaciones")
	print("===========")
	print("[ 0 ] Salir")
	print("[ 1 ] Adición")
	print("[ 2 ] Sustracción")
	print("[ 3 ] Multiplicación")
	operador = int(input("Operación: "))
	if operador == 0:
		break
	operando = int(input("Operando: "))
	if operador == 1:
		C = C + operando
		operaciones = operaciones + " + " + str(operando)
		continue
	elif operador == 2:
		C = C - operando
		operaciones = operaciones + " - " + str(operando)
		continue
	elif operador == 3:
		C = C * operando
		operaciones = "( " + operaciones + " ) * " + str(operando)
		continue

# =============================================================================
# C luego de las operaciones
# =============================================================================
print()
print("Resumen")
print("=======")
print("N inicial:", N)
print("C inicial:", C_ini)
print()
print("Operaciones:", operaciones, " = ", C)

# =============================================================================
# Descifrar el número C
# =============================================================================
NN = hm.decrypt(C)
print()
print("C desencriptado:", NN)
