CALCULADORA DE CONSUMO ELÉTRICO


A Calculadora de Consumo Elétrico é um programa desenvolvido em Python que permite estimar o consumo mensal de energia elétrica de um aparelho.
O usuário informa o nome do aparelho, sua potência em watts e o tempo médio de utilização diária. A partir dessas informações, o programa calcula o consumo estimado em kWh por mês.
Além disso, o sistema apresenta uma estimativa do custo mensal da energia utilizando uma tarifa fixa de R$ 0,75 por kWh.
O consumo mensal é calculado utilizando a seguinte fórmula:

Consumo mensal = potencia x horas por dia x 30 / 1000
Onde:
potencia = potência do aparelho em watts (W)
horasDia = quantidade média de horas de utilização por dia
30 = quantidade aproximada de dias no mês
1000 = conversão de Wh para kWh

Para calcular o custo estimado:
Custo mensal = consumo mensal x tarifa
Neste projeto, foi utilizada uma tarifa de referência de R$ 0,75 por kWh.

Como executar:
1. Clone o repositório
git clone URL_DO_SEU_REPOSITORIO
2. Acesse a pasta do projeto
cd consumo-energia
3. Execute o programa
python app.py

💻 Tecnologias utilizadas
🐍 Python
🐙 GitHub
💡 Cálculo de consumo de energia elétrica