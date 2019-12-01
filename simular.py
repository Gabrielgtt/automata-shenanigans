import sys
from automato import Automato

if __name__ == "__main__":
	arquivo_automato, palavra_input = sys.argv[1], sys.argv[2]
	automato = Automato.ler_automato(arquivo_automato)
	automato.checar_pertencimento(palavra_input)
