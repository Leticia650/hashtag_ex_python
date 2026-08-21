print("########### Exercício 1")
"""
Exercício 1: Dashboard de Vendas (Análise de Dados) Você recebeu uma lista com as 
vendas diárias de uma equipe: vendas = [1500, 2000, 800, 3500, 1200]. Crie um 
programa que exiba um pequeno relatório contendo: 
1. O total de vendas na semana. 
2. A média de vendas diária. 
3. O valor da melhor venda e da pior venda do período.

"""

vendas = [1500, 2000, 800, 3500, 1200]
total_vendas = sum(vendas)
qtde_dias = len(vendas)
media_vendas = total_vendas / qtde_dias
maior_venda = max(vendas)
menor_venda = min(vendas)

print(f"Total de vendas: {total_vendas}")
print(f"Média de vendas: {media_vendas}")
print(f"Maior quantidade de vendas: {maior_venda}")
print(f"Menor quantidade de vendas: {menor_venda}")


print("########### Exercício 2")
"""
Exercício 2: Gestão de Estoque (Edição e Verificação) Uma loja de eletrônicos possui os 
seguintes produtos: estoque = ["monitor", "teclado", "mouse", "headset"]. 
O gerente pediu para: 
1. Adicionar o item "webcam" ao final da lista. 
2. O "teclado" teve seu nome atualizado para "teclado mecanico". Faça essa 
alteração na lista. 
3. Verificar se "impressora" está no estoque. O programa deve exibir True ou 
False. 
4. Remover o "mouse" da lista, pois saiu de linha. 

"""

estoque = ["monitor", "teclado", "mouse", "headset"]
estoque.append("webcam")
posicao_teclado = estoque.index("teclado")
estoque[posicao_teclado] = "teclado mecânico"
impressora = "impressora" in estoque 
print(estoque)
print(impressora)
estoque.remove("mouse")
print(estoque)