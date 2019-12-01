import sys
from automato import Automato

if __name__ == "__main__":
	arquivo_automato1, arquivo_automato2 = sys.argv[1], sys.argv[2]
	automato1 = Automato.ler_automato(arquivo_automato1)
	automato2 = Automato.ler_automato(arquivo_automato2)
	automato_uniao = automato1.uniao(automato2)
	print(automato_uniao)
