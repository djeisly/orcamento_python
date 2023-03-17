#!/usr/bin/env python
# coding: utf-8

# # Meu primeiro código Python

# # Entrada de dados

# In[2]:


input("Digite a descrição do projeto:")
input("Digite a quantidade de horas estimadas:")
input("Digite o valor da hora trabalhada:")
input("Digite o prazo:")


# # Guardando os dados

# In[3]:


projeto = input("Digite a descrição do projeto:")
horas_estimadas = input("Digite a quantidade de horas estimadas:")
valor_hora = input("Digite o valor da hora trabalhada:")
prazo = input("Digite o prazo:")


# In[4]:


print(prazo)


# # Cálculo

# In[5]:


valor_total = int(horas_estimadas) * int(valor_hora)


# # Gerando o PDF do Orçamento

# In[7]:


get_ipython().system('pip install fpdf')


# In[8]:


from fpdf import FPDF


# In[15]:


pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png", x=0, y=0)
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output("Orçamento Python.pdf")
print("Orçamento gerado com sucesso")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




