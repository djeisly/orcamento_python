# Projeto de Orçamento
Este é um projeto em Python para estimar o custo de um determinado projeto com base nas horas de trabalho presumidas, valor da hora trabalhada, prazo para entrega e valor total. O projeto gera um documento com o orçamento detalhado em um modelo definido. 

  

## Funcionamento

O projeto consiste em uma classe Orçamento que recebe as seguintes entradas:

Horas estimadas de trabalho: quantidade de horas que serão necessárias para concluir o projeto.
Valor da hora trabalhada: valor cobrado por hora de trabalho.
Prazo para entrega: limite de dados para entrega do projeto.

Com base nesses insumos, uma classe realiza o calculado do valor total do projeto e gera um documento com o orçamento detalhado em um modelo definido.

  

## Requisitos

* Python 3.6 ou superior

* Bibliotecas: Pandas

## Como usar

Clone o repositório em sua máquina local

Instale a biblioteca necessária: pip install pandas

Importe uma classe Orçamento para o seu projeto: from orçamento import Orçamento

Crie uma instância da classe Orçamento com as entradas necessárias: orcamento = Orcamento(horas_estimadas, valor_hora, prazo_entrega)

Acesse o atributo valor total para obter o valor total do projeto: 
valor_total = orcamento.valor_total

Acesse o método gerar orcamento para gerar o documento do orçamento:orcamento.gerar_orcamento()

## Exemplo de uso

  
```python
from orcamento import Orcamento
horas_estimadas = 50
valor_hora = 100
prazo_entrega = '2023-04-30'
orcamento = Orcamento(horas_estimadas, valor_hora, prazo_entrega)
valor_total = orcamento.valor_total
orcamento.gerar_orcamento()
```