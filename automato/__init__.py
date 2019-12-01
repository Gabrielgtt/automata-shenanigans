class Automato:
	"""
		Recebe um dicionário com os estados do autômato.
		Cada estado é uma string que deve estar relacionado a uma lista de tuplas do tipo (a, B), indicando que ao ler "a", nesse estado, vamos para B.
		Recebe ainda uma lista com os estados finais e por fim o estado inicial.
	"""
	def __init__(self, estados, finais, inicio):
		self.estados = estados
		self.inicio = inicio
		self.finais = finais

	"""
		Lê e retorna um autômato do arquivo_automato no seguinte padrão:
			estados A, B
			inicial A
			aceita B
			A B 0
			B A 0
			A A 1
			B B 1
	"""
	def ler_automato(arquivo_automato):
		estados = {}
		finais = []
		inicio = 'A'

		with open(arquivo_automato, 'r') as inputFile:
			for cnt, linha in enumerate(inputFile):

				# Leitura dos estados
				if cnt == 0:
					for pal in linha.split()[1:]:
						estados[pal[:-1] if pal[-1] == ',' else pal] = []

				# Leitura do estado inicial
				elif cnt == 1:
					inicio = linha.split()[1]

				# Leitura dos estados de aceitacao
				elif cnt == 2:
					for pal in linha.split()[1:]:
						finais.append(pal[:-1] if pal[-1] == ',' else pal)

				# Leitura das transicoes
				else:
					de, para, ent = linha.split()
					estados[de].append((ent, para))

		return Automato(estados, finais, inicio)

	"""
		Método auxiliar de checar pertencimento
		Recursivamente percorre os estados do automato enquanto itera sobre uma palavra
		Caso a execução termine em um estado final (de aceitação) return true, do contrário, false.
	"""
	def aceita(self, idx, palavra, estadoAtual):
		palavraRestante = "e" if idx == len(palavra) else palavra[idx:]
		print("{0}                {1}".format(estadoAtual, palavraRestante))

		if idx == len(palavra):
			return estadoAtual in self.finais

		deu = False
		for caracter, novoEstado in self.estados[estadoAtual]:
			if caracter == palavra[idx]:
				deu = deu or self.aceita(idx+1, palavra, novoEstado)

		return deu

	""" Checa o pertencimento de uma palavra no autômato. """
	def checar_pertencimento(self, palavra):
		print("Estado                Palavra")
		aceitou = self.aceita(0, palavra, self.inicio)
		print("")
		if aceitou:
			print("A palavra foi aceita")
		else:
			print("A palavra não foi aceita")


	"""
		Retorna uma cópia do autômato com os estados adicionados de "*" ao final de cada um.
		Usado para evitar intersecção de nomes na união de autômatos.
	"""
	def converter(self):
		inicio = self.inicio + "*"
		finais = [x+"*" for x in self.finais]
		estados = {}
		for estado in list(self.estados):
			estados[estado+"*"] = [(x, y+"*") for (x, y) in self.estados[estado]]
		return Automato(estados, finais, inicio)


	""" Retorna a união com outro autômato.	"""
	def uniao(self, automato):
		automato.converter()
		inicio = self.inicio + automato.inicio
		finais = self.finais + automato.finais
		novos_estados = self.estados.copy()
		novos_estados.update(automato.estados)
		novos_estados.update({inicio: [("e", self.inicio), ("e", automato.inicio)]})
		return Automato(novos_estados, finais, inicio)


	""" Retorna o autômato complemento desse. """
	def complemento(self):
		estados_intermediarios = [x for x in list(self.estados) if x not in self.finais]
		return Automato(self.estados.copy(), estados_intermediarios, self.inicio)


	def __str__(self):
		str_automato = ""
		str_automato += "Estado inicial: {0}\n".format(self.inicio)
		str_automato += "Transições: \n"
		for estado, transicoes in self.estados.items():
			for entrada, destino in transicoes:
				str_automato += "{0} -- {1} --> {2}\n".format(estado, entrada, destino)
		str_automato += "Estados finais: {}".format(", ".join(self.finais))
		return str_automato
