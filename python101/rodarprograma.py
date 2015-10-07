"""
Pergunta e calcula estatísticas de idade dos lista_entrevistados

Este código é dividido em quatro partes a seguir:
1a. parte: ler o arquivo json - carrega_dados()
2a. parte: fazendo novas perguntas - novos_dados()
3a. parte: salvando tudo no arquivo - salvar_dados()
4a. parte: calculando e mostrando as estatisticas - calcular_dados()
"""

from python101 import meuprograma
import statistics
import json
import sh

lista_entrevistados = []

def carrega_dados():
	"""
	Carrega as informações do arquivo JSON.

	Popula a lista lista_entrevistados com instancias da classe
	Entrevista com os valores que vem do arquivo JSON
	"""

	global lista_entrevistados

	def pega_dados(obj):
		"""
		Cria uma instancia nova de Entrevista.

		Usa os dados vindos do json através do objeto 'obj'
		para nome, idade e ano_informado
		Retorna a instancia Entrevista()
		"""
		instancia = meuprograma.Entrevista(
				nome=obj['nome'],
				idade=obj['idade'],
				ano=obj['ano']
			)
		return instancia

	try:
		arquivo_json = open('python101/dados.json','r') # Abre o arquivo no disco
		dados_json = json.load(arquivo_json) # Converte dicionario Json -> Python
		entrevistas = dados_json['Entrevistas']

		lista_entrevistados = [ pega_dados(entrevista) for entrevista in entrevistas ]
	except Exception as erro:
		print("Ocorreu um erro ao carregar o arquivo.")
		print("O erro é: {}".format(erro))

def novos_dados():
	"""
	Pergunta novos nomes e anos de nascimentos.

	Enquanto o usuário não digitar 'parar' ao perguntado o nome
	o programa pergunta o ano de nascimento e calcula a idade
	"""
	pode_parar = False

	while pode_parar == False:
		entrevistado = meuprograma.Entrevista()
		if entrevistado.pergunta_nome().lower() == "parar": # Parar PARAR pARAR
			pode_parar = True
		else:
			try:
				entrevistado.pergunta_idade()
				x = 1000 / entrevistado.ano_informado
			except ZeroDivisionError:
				print('Ocorreu um erro mas a lista foi salva')
				lista_entrevistados.append(entrevistado)
			except Exception as erro:
				print('Ocorreu um erro e a lista NÃO foi salva')
				print('O tipo de erro foi {}'.format(type(erro)))
				print('A mensagem foi {}'.format(erro))
			else:
				lista_entrevistados.append(entrevistado)

def salvar_dados():
	"""
	Salva as informações geradas num arquivo Json.

	Converte o dicionario Python para JSON e salva os dados
	da lista 'lista_entrevistados'

	Cria a lista no formato [{ nome=obj.nome, ano=obj.ano, idade=obj.idade }]
	Transforma a lista em um dicionário { "Entrevistas": lista } 
	"""
	
	lista_salvar = [
		dict(nome=obj.nome, ano=obj.ano_informado, idade=obj.idade)
		for obj in lista_entrevistados
	]

	dict_salvar = { "Entrevistas": lista_salvar }
	dict_salvar = json.dumps(dict_salvar, indent=4, sort_keys=False)

	try:
		arquivo_json = open("python101/dados.json", "w") # Abre o arquivo e limpa
		arquivo_json.write(dict_salvar) # Escreve os dados no arquivo
		arquivo_json.close() # Fecha e salva o arquivo
	except Exception as erro:
		print("Ocorreu um erro ao carregar o arquivo.")
		print("O erro é: {}".format(erro))

def calcular_dados():
	"""
	Calcula as estatisticas de idade:

	1. Mostrar a menor idade calculada
	2. Mostrar a maior idade calculada
	3. Mostrar a média de idade dos adultos
	4. Mostrar a quantidade de nascimentos por década

	O que temos: [ 1970, 1981, 1998, 2002, 1990, 1970 ]
	O que queremos: { 1980: 10, 1990: 15, 2000: 5 }

	1o passo: converter anos em decadas:
	1985 / 10 = 198,5 int -> 198 x10 = 1980
	2o passo: criar uma lista nova (set_decadas) com as decadas sem repetir
	3o passo: contar as decadas na lista original (lista_decadas) usando a lista nova
	Para cada decada dentro da lista nova (set_decadas) contar qtas vezes
	ela aparece na lista original (lista_decadas)
	"""

	# Lista por Compreensão
	# lista = [ <expressão para valor> <loop> <expressão para loop> ]
	menor_idade = min([ objeto.idade for objeto in lista_entrevistados ])
	maior_idade = max([ objeto.idade for objeto in lista_entrevistados ])

	media_adultos = statistics.median_high(
			[ objeto.idade for objeto in lista_entrevistados if objeto.idade >= 18 ]
		)

	lista_decadas = [ int(objeto.ano_informado/10)*10 for objeto in lista_entrevistados]

	set_decadas = set(lista_decadas)

	# Dicionário por Compreensão
	# dicionario = { <expressao para chave>:<expressao para valor> <loop> <expressao pro loop>}
	qtd_nascimentos = { decada:lista_decadas.count(decada) for decada in set_decadas }

	print("\nResultados:")
	print('-----------------------------------------')
	print("Quantidade de Entrevistas: {}".format(len(lista_entrevistados)))
	print("Menor Idade Informada: {}".format(menor_idade))
	print("Maior Idade Informada: {}".format(maior_idade))
	print("Média de Idade dos Adultos Informados: {}".format(media_adultos))
	print("\nNascimentos por Década")
	print('-----------------------------------------')
	for decada, quantidade in qtd_nascimentos.items():
		print("{}: {} nascimentos".format(decada, quantidade))
	print('\n\n')

	resposta_ok = False

	while resposta_ok == False:
		try:
			resposta = input("Deseja mostrar os dados num arquivo? (s/n)")
			resposta = resposta[0].lower()
			if resposta == 's' or resposta == 'n':
				resposta_ok = True
		except:
			continue

	if resposta == 's':
		sh.gedit("dados.json")

def main():
	carrega_dados()
	novos_dados()
	salvar_dados()
	calcular_dados()


