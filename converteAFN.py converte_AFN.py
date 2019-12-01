import sys
from automato import Automato

def mask_possui_estado(mask, estado):
	return (mask & (1 << estado)) != 0

def mask_to_str(mask, n, itoe):
	result = ''
	for i in range(n):
		if mask_possui_estado(mask, i):
			result += itoe[i]
	return result

def converteNFA(automato):
	estados = automato.estados.copy()
	finais = automato.finais.copy()
	inicio = automato.inicio
	n = 0
	masksE = {}
	etoi = {}
	itoe = {}

	for e in estados:
		etoi[e] = n
		itoe[n] = e
		n += 1

	for e in estados: masksE[e] = (1 << etoi[e])

	finalizado = False
	while not finalizado:
		finalizado = True

		for e in estados:
			for caractere, estado in estados[e]:
				if caractere == 'e':
					velha_mask = masksE[e]
					masksE[e] |= masksE[estado]
					finalizado = finalizado and (velha_mask == masksE[e])

	estadosF = estados
	finaisF = []
	inicioF = mask_to_str( (1 << etoi[inicio]) | masksE[inicio], n, itoe)

	for mask in range(1 << n):
		mask_str = mask_to_str(mask, n, itoe)
		transicoes = ''

		for estado in mask_str:
			for transicao in estados[estado]:
				if transicao[0] == 'e': continue
				if transicao[0] in transicoes: continue
				transicoes += transicao[0]

		for char in transicoes:
			goToMask = 0
			for i in range(n):
				if mask_possui_estado(mask, i):
					e = itoe[i]
					for caractere, novo_estado in estados[e]:
						if caractere == 'e' or len(novo_estado) > 1: continue
						if caractere == char:
							goToMask |= (1 << etoi[novo_estado])

			fo_to_mask_str = mask_to_str(goToMask, n, itoe)

			if mask_str not in estadosF: estadosF[mask_str] = []
			estadosF[mask_str].append( (char, fo_to_mask_str) )

		for est_final in finais:
			if est_final in mask_str:
				finaisF.append(mask_str)
				break

	return Automato(estadosF, finaisF, inicioF)


if __name__ == "__main__":
	arquivo_automato = sys.argv[1]
	automato = Automato.ler_automato(arquivo_automato)
	print(converteNFA(automato))
