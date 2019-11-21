a = 3
b = 15

def converte_velocidade(km_h):
  metros = km_h * 1000
  segundos = 1 * 60 * 60
  print(a) # 3
  # print(c) # not_defined
  # global b
  # b = 28
  return metros/segundos

vel_m_s = converte_velocidade(72)
print(vel_m_s)

print(b) # 15 (com global fica 28)
c = 4

# print(km_h) # not_defined
# print(metros) # not_defined
# print(segundos) # not_defined
