"""
Módulo que contém a classe Entrevista.

Esta classe será usada para instanciar e guardar cada Entrevista
feita pelo programa mais as entrevistas guardadas em disco

Os dados dessas instancias serão usados para fazer as estatísticas
"""


import datetime
	
class Entrevista():
	""" Classe Entrevista """

	def __init__(self, nome="", idade=0, ano=0):
		"""
		Entra com os valores iniciais. Váriaveis de sistema:

		nome = nome informado pelo entrevistado
		ano = ano de nascimento informa pelo entrevistado
		idade = idade calculada do entrevistado
		"""
		super(Entrevista, self).__init__()
		self.nome = nome
		self.idade = idade
		self.ano_informado = ano

	def __eq__(self, other):
		"""
		Compara duas instancias desse objeto.

		Retorna verdadeiro se nome, idade e ano informado forem iguais.
		"""
		return self.nome == other.nome and self.idade == other.idade and self.ano_informado == other.ano_informado

	def pergunta_nome(self):
		""" Pergunta o nome do entrevistado. Retorna um string. """
		nome_ok = False
		while nome_ok == False:
			self.nome = input("Qual é o seu nome?"
				"(digite 'parar' para parar) ")
			if self.nome:
				nome_ok = True
				if self.nome.lower() != "parar":
					print('O seu nome é "' + self.nome + '"')
		
		self.nome = self.nome.title()

		return self.nome

	def pergunta_idade(self):
		"""
		Pergunta o ano de nascimento e calcula a idade.

		Pergunta o ano de nascimento e valida o valor entre 1900
		e o ano atual, calculado através de datetime.date.today().year
		Se validado, calcula a idade
		"""
		ano_atual = datetime.date.today().year
		ano_ok = False

		while ano_ok == False:
			try:
				# Perguntar em que ano você nasceu
				self.ano_informado = int(input("Ei " + self.nome + ", em que ano você nasceu? "))
				ano_ok = True
			except:
				continue
			else:
				if self.ano_informado >= 1900 and self.ano_informado <= ano_atual:
					pass
				else:
					ano_ok = False
		
		# Subtrair o ano atual do ano informado
		self.idade = ano_atual - self.ano_informado
		# imprimir na tela a idade calculada
		print("Você tem",self.idade,"anos.")
			
		
	def __str__(self):
		""" Retorna uma descrição amigável do objeto """
		return "{}/{}".format(self.nome, self.idade)

	def __repr__(self):
		""" Retorna uma descrição precisa e única do objeto """
		return "input()={} input()=int({})".format(self.nome, self.idade)


				