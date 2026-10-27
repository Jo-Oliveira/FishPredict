from src.databases import peixes_dic, locais_dic
from src.recomendacao import nota_temperatura, indice, nota_ondulacao, nota_vento
from src.services import obter_tempo
from src.models import Condicoes


# while True:
#     print("-- APP DE PESCA --")
#     print("1 - Ver todos os peixes: ")
#     print("2 - Ver peixes por nome")
#     print("3 - Ver tempo para pescar")
#     print("4 - Sair")
#
#     opcao = input("Escolher uma opção: ")
#
#     match opcao:
#         case "1":
#              for peixe in peixes_dic.values():
#                  print(f"Peixe: {peixe.nome}")
#         case "2":
#              nome_peixe = input("Insira o nome do peixe: ").lower().strip()
#
#              if nome_peixe not in peixes_dic:
#                     print("Peixe não encontrado na base de dados.")
#              else:
#                     peixe = peixes_dic[nome_peixe]
#                     print(f"\n--- {peixe.nome} ({peixe.nome_cientifico}) ---")
#                     print(f"Habitat: {peixe.habitat}")
#                     print(f"Técnica: {peixe.tecnica}")
#                     print(f"Amostra ideal: {peixe.amostra_ideal}")
#                     print(f"Tamanho mínimo: {peixe.tamanho_minimo_cm} cm\n")
#                     print(f"Época para pescar: {peixe.epoca_pesca}")
#                     print(f"Melhor hora do dia: {peixe.melhor_hora_dia}")
#                     print(f"Condições de vento favoráveis: {peixe.condicoes_vento_ideais} ")
#                     print(f"Fase da maré: {peixe.fase_mare_ideal}")
#                     print(f"Condições de ondulação: {peixe.condicoes_ondulacao_ideal}")
#                     print(f"Tipo de água: {peixe.tipo_agua}")
#                     print(f"Profundidade ideal: {peixe.profundidade_ideal}")
#                     print(f"Temperatura da água: {peixe.temperatura_da_agua}")
#                     print(f"Fase lunar: {peixe.fase_lunar}")
#         case "3":
#             # latitude = input("Insira o latitude: ").strip()
#             # longitude = input("Insira o longitude: ").strip()
#             local = input("Insira o local: ")
#
#             if local not in locais_dic:
#                     print("O local indicado não foi encontrado.")
#             else:
#                 local = locais_dic[local]
#                 print(f"\n--- {local.nome} ---")
#                 print(f"Latitude: {local.latitude}")
#                 print(f"Longitude: {local.longitude}")
#                 print(f"Tipo de agua: {local.tipo_de_agua}")
#                 print("Peixes comuns: \n")
#                 for peixe in local.peixes_comuns:
#                     print(f"Peixe: {peixe.nome}")

condicoes = Condicoes(temperatura_agua=19.0, vento=12.0, ondulacao=1.5)
# print(condicoes)
robalo = peixes_dic['robalo']
print(f"Temperatura: {round(nota_temperatura(robalo, condicoes))}/100")
print(f"Ondulação: {round(nota_ondulacao(robalo, condicoes))}/100")
print(f"Vento: {round(nota_vento(robalo, condicoes))}/100")


condicoes = Condicoes(temperatura_agua=16.0, vento=17.5, ondulacao=1.0)
# print(condicoes)
robalo = peixes_dic['robalo']
print(f"Temperatura: {round(nota_temperatura(robalo, condicoes))}/100")
print(f"Ondulação: {round(nota_ondulacao(robalo, condicoes))}/100")
print(f"Vento: {round(nota_vento(robalo, condicoes))}/100")

print(f"Classificação: {round(indice(robalo, condicoes))}%")