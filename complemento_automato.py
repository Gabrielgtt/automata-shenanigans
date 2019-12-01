import sys
from automato import Automato

if __name__ == "__main__":
	arquivo_automato = sys.argv[1]
	automato = Automato.ler_automato(arquivo_automato)
	print(automato.complemento())
