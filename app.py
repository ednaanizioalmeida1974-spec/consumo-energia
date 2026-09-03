print("=== CALCULADORA DE CONSUMO DE ENERGIA ===")

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite quantas horas por dia ele é utilizado: "))

consumo_mensal = (potencia * horas_dia * 30) / 1000

print("\n=== RESULTADO ===")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")