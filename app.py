aparelho=input("digite o nome do aparelho")
potencia=float(input("digite a potencia do aparelho em watts (W):"))
horas_dia=float(input("digite o tempo medio de uso diario (em horas):"))
consumo_mensal=(potencia*horas_dia*30)/1000
tarifa=0.75
custo_mensal= consumo_mensal * tarifa
print(f"aparelho: {aparelho}")
print(f"consumo estimado: {consumo_mensal:.2f} kwh/mes")
print(f"custo estimado: R${custo_mensal:.2f}")