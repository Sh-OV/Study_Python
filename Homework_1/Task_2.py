# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#  РЕШЕНИЕ 1:
for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)
                
# РЕШЕНИЕ 2:
def XYZ (x, y, z):
    return (not (x or y or z)) == (not x and not y and not z)

if (XYZ(0, 0, 0) and XYZ(0, 0, 1) and XYZ(0, 1, 0) and 
XYZ(0, 1, 1) and XYZ(1, 0, 0) and XYZ(1, 0, 1) and
XYZ(1, 1, 0) and XYZ(1, 1, 1)):
    print("TRUE")
else:
    print("FALSE")