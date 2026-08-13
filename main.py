from src.databases import peixes_dic
from src.services import obter_tempo

for peixe in peixes_dic.values():
    print(f"🐟 {peixe.nome} ({peixe.nome_cientifico}):")
    print(f"    Tamanho mínimo legal: {peixe.tamanho_minimo_cm} cm")
    print(f"    Técnica ideal: {peixe.tecnica} \n")

while True:
    print("-- APP DE PESCA --")
    print("1 - Ver todos os peixes: ")
    print("2 - Ver peixes por nome")
    print("3 - Ver tempo para pescar")
    print("4 - Sair")

    opcao = input("Escolher uma opção: ")

    match opcao:
        case "1":
             for peixe in peixes_dic.values():
                 print(f"Peixe: {peixe.nome}")
        case "2":
             nome_peixe = input("Insira o nome do peixe: ").lower().strip()

             if nome_peixe not in peixes_dic:
                    print("Peixe não encontrado na base de dados.")
             else:
                    peixe = peixes_dic[nome_peixe]
                    print(f"\n--- {peixe.nome} ({peixe.nome_cientifico}) ---")
                    print(f"Habitat: {peixe.habitat}")
                    print(f"Técnica: {peixe.tecnica}")
                    print(f"Amostra ideal: {peixe.amostra_ideal}")
                    print(f"Tamanho mínimo: {peixe.tamanho_minimo_cm} cm\n")
                    print(f"Época para pescar: {peixe.epoca_pesca}")
                    print(f"Melhor hora do dia: {peixe.melhor_hora_dia}")
                    print(f"Condições de vento favoráveis: {peixe.condicoes_vento_ideais} ")
                    print(f"Fase da maré: {peixe.fase_mare_ideal}")
                    print(f"Condições de ondulação: {peixe.condicoes_ondulacao_ideal}")
                    print(f"Tipo de água: {peixe.tipo_agua}")
                    print(f"Profundidade ideal: {peixe.profundidade_ideal}")
                    print(f"Temperatura da água: {peixe.temperatura_da_agua}")
                    print(f"Fase lunar: {peixe.fase_lunar}")
        case "3":
            # latitude = input("Insira o latitude: ").strip()
            # longitude = input("Insira o longitude: ").strip()
            latitude = 38.7223
            longitude = -9.1393

            tempo = obter_tempo(latitude, longitude)

            if tempo:
                print(f"\n--- Condições Atuais ---")
                print(f"Temperatura: {tempo['temperatura']} °C")
                print(f"Vento: {tempo['vento']} km/h")
                print(f"Ondulação: {tempo['ondas']} m")
            else:
                print("Não foi possível obter os dados do tempo.")
        case "4":
            break
        case _:
            print("Opção inválida, tenta novamente.")