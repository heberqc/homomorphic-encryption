# -*- coding: utf-8 -*-

# =============================================================================
# Choose J (64bit), K(16bit)
# =============================================================================

J = 14883982794894487223
K = 43321

# =============================================================================
# D and F (256-bit) randomly
# =============================================================================

D = 70677186543966147614195862042065680704217811307170938823680817972460078770747
F = 73039047329961611877474622320644292204439326844747783070676806904287578243639

# =============================================================================
# Choose 4 bit random integer K1
# =============================================================================

K1 = 12

# =============================================================================
# P0 = JD
# P1 = JF + KK1
# =============================================================================

P0 = J * D
P1 = J * F + K * K1

# =============================================================================
# Accept Number N from user
# =============================================================================

N = 90

# =============================================================================
# P2 = [ T1 P1 ] mod P0
# 
# Encryption
# Cipher Text C = [N+ T2 P2] mod P0
# (T1 , T2 are a 4-bit random integer)
# =============================================================================

T1, T2 = 5, 9

P2 = (T1 * P1) % P0

C = (N + T2 * P2) % P0

# =============================================================================
# Decryption
# N = (C mod J) mod K
# =============================================================================

N1 = (C % J) % K