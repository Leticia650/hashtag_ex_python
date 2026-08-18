"""

Exercício 1 — Cálculo de Comissão de Vendas
Área: RH / Vendas
Cenário: Uma empresa decidiu pagar uma comissão de 8% sobre o faturamento total de uma equipe de
vendas. O objetivo é calcular o valor da comissão e descobrir quanto sobra do faturamento depois do
pagamento.
Dados:
• Faturamento inicial: R$ 72.000,00
• Percentual de comissão: 0,08
O que você precisa fazer:
1. Crie as variáveis necessárias.
2. Calcule o valor da comissão.
3. Calcule o faturamento final após descontar a comissão.
4. Exiba os dois resultados.
Foco do exercício: Operações com porcentagem, multiplicação e subtração.
Desafio extra: depois de resolver, tente alterar novamente os valores das variáveis e confira se seu código
continua funcionando co

"""
print("#################Exercicíco 1 da folha gerada por inteligencia artificial")

perc_comissao = 0.08
fat_in = 72000
comissao = perc_comissao * fat_in
print(f"O valor da comissao é de: {comissao}")
fat_fin = fat_in - comissao
print(f"O valor do faturamento final é de: {fat_fin}")

print("########## Exercío 2")

"""
Exercício 2 — Controle de Estoque de Loja Online
Área: Logística / E-commerce
Cenário: Uma loja online começou o dia com 320 unidades de um determinado produto em estoque. Ao
longo do dia, foram vendidas 95 unidades e chegaram mais 140 unidades do fornecedor.
Dados:
• Estoque inicial: 320 unidades
• Vendas: 95 unidades
• Entrada do fornecedor: 140 unidades
O que você precisa fazer:
1. Crie uma variável para representar o estoque.
2. Subtraia as unidades vendidas.
3. Some as unidades recebidas.
4. Exiba o estoque final.
Foco: Atualização de variáveis, som

"""

estoque = 320
vendas = 95
reposicao = 140
estoque = (estoque - vendas) + reposicao
print(f"A quantidade de produtos disponíveis em estoque é de: {estoque}")


print("########### Exercicío 3")

"""
Exercício 3 — Divisão de Cargas
Área: Logística / Transporte
Cenário: Uma transportadora precisa enviar 987 caixas usando caminhões pequenos. Cada caminhão
suporta exatamente 15 caixas.
Dados:
• Total de caixas: 987
• Capacidade de cada caminhão: 15 caixas
O que você precisa fazer:
1. Calcule quantos caminhões ficarão totalmente cheios usando o operador //.
2. Calcule quantas caixas sobrarão usando o operador %.
3. Exiba os dois resultados.
Foco: Divisão inteira (//) e resto da divisão (%).

"""

caixas = 987
capac_caminhoes = 15

viagem = caixas // capac_caminhoes
print(f"A quantidade de caminhões completos é de: {viagem} ")

rest = caixas % capac_caminhoes
print(f"Ficarão {rest} unidades de caixas no caminhão incompleto")


print("######### Exercício 4")

"""
Exercício 4 — Análise de Margem de Lucro
Área: Financeiro
Cenário: Uma pequena empresa faturou R$ 22.000,00 em um projeto. Os custos fixos foram de R$
7.500,00 e o imposto sobre o faturamento é de 12%.
Dados:
• Faturamento: R$ 22.000,00
• Custos fixos: R$ 7.500,00
• Imposto: 0,12
O que você precisa fazer:
1. Calcule o valor do imposto.
2. Calcule o lucro líquido considerando o faturamento, o imposto e os custos fixos.
3. Calcule a margem de lucro usando a fórmula: lucro / faturamento.

"""
faturamento = 22000
custos_f = 7500
perc_imposto = 0.12
imposto = faturamento * perc_imposto
lucro_liquido = faturamento - custos_f - imposto
margem_lucro = lucro_liquido / faturamento
meta_atingida = margem_lucro > 0.30

print(f"A meta foi atingida? {meta_atingida} ")
print(f"A margem de lucro é de: {margem_lucro:.2f}")
print(f"O valor do imposto é de: {imposto}")
print(f"O lucro liquido é de {lucro_liquido}")


print("######### Exercício 5")
"""
Exercício 5 — Conversão de Tempo de Contrato
Área: Gestão de Projetos
Cenário: Um contrato de suporte técnico possui duração de 53 meses. O cliente deseja visualizar esse
período no formato: "X anos e Y meses".
Dados:
• Duração do contrato: 53 meses
• 1 ano = 12 meses
O que você precisa fazer:
1. Use // para descobrir quantos anos completos existem.
2. Use % para descobrir quantos meses sobram.
3. Monte uma mensagem informando o resultado no formato solicitado.
4. Exiba a mensagem.
Foco: Divisão inteira (//), resto (%) e montagem de strings.

"""

contrato = 53 
ano = 12
duracao_contrato = contrato // ano 
meses_restantes = contrato % ano
print(f"O contrato possui a duração de {duracao_contrato:.0f} anos e {meses_restantes} meses.")
