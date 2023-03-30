qtde = int(input("informe a quantidade comprada :"))
valorunit = float(input(" informe o valor unitario:"))
desconto = float(input(" informe o desconto:"))

totalsemdesconto = qtde* valorunit
valordesconto = totalsemdesconto * desconto/100
totalcomdesconto = totalsemdesconto - valordesconto

print(f"o total sem descoto sera R$ {totalsemdesconto:.2f}")
print(f"o valor do desconto sera R$ {valordesconto:.2f}")
print(f" o valor com desconto sera R$ {totalcomdesconto:.2f}")
