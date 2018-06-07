import secrets

# =============================================================================
# Funciones de encriptación homomórfica
# =============================================================================

J = 14883982794894487223
K = 43321

def generateSecretKeys():
	global J
	global K
	J = secrets.randbits(64) + 1
	K = secrets.randbits(16) + 1

def getSecretKeys():
	return J, K

def encrypt(N):
	D = secrets.randbits(256) + 1
	F = secrets.randbits(256) + 1
	K1 = secrets.randbits(4) + 1
	P0 = J * D
	P1 = J * F + K * K1
	T1, T2 = secrets.randbits(4) + 1, secrets.randbits(4) + 1
	P2 = (T1 * P1) % P0
	C = (N + T2 * P2) % P0
	return C

def decrypt(C):
	N = (C % J) % K
	return N
