# A = [3, 8]
# B = [6, 10]

# A:  3 ───────────── 8
# B:         6 ───────────── 10

# Há intesecção porque: início de A <= final de B.     3 <= 10. True
#                       início de B <= final de A.     6 <= 8.  True

# Genericamente:
# A = [a0, a1]
# B = [b0, b1]
# Há intesecção quando (a0 <= b1) and (b0 <= a1)


valores = list(map(int, input().split()))

# Retângulo A
ax0 = valores[0]
ay0 = valores[1]
ax1 = valores[2]
ay1 = valores[3]

# Retângulo B
bx0 = valores[4]
by0 = valores[5]
bx1 = valores[6]
by1 = valores[7]

# Verificar os máximos e mínimos
a_min_x = min(ax0, ax1)
a_max_x = max(ax0, ax1)
a_min_y = min(ay0, ay1)
a_max_y = max(ay0, ay1)

b_min_x = min(bx0, bx1)
b_max_x = max(bx0, bx1)
b_min_y = min(by0, by1)
b_max_y = max(by0, by1)

# Verifica as intersecções
intersecao_x = (a_min_x <= b_max_x) and (b_min_x <= a_max_x)
intersecao_y = (a_min_y <= b_max_y) and (b_min_y <= a_max_y)

if intersecao_x and intersecao_y:
    print(1) # Saída 1 quando há colisão
else:
    print(0) # Saída 0 quando não há colisão