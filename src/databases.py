from src.models import Peixe, LocalPesca

peixes_dic = {
    "robalo": Peixe(
        nome="Robalo",
        nome_cientifico="Dicentrarchus labrax",
        habitat="Rebentação / Zonas de rocha e areia",
        tecnica="Spinning",
        amostra_ideal="Amostra rija / Vinil",
        tamanho_minimo_cm=36,
        epoca_pesca=[9, 10, 11, 12, 1, 2, 3],
        melhor_hora_dia=[(6, 9), (18, 21)],
        condicoes_vento_ideais=(10.0, 25.0),
        fase_mare_ideal="vazante",
        condicoes_ondulacao_ideal=(0.5, 1.5),
        tipo_agua="Mar aberto / Estuário",
        profundidade_ideal=3.0,
        temperatura_da_agua=(12.0, 20.0),
        fase_lunar="cheia ou nova"
    ),
    "dourada": Peixe(
        nome="Dourada",
        nome_cientifico="Sparus aurata",
        habitat="Fundos de areia, Lodo, estuários e rias",
        tecnica="Surfcasting / Chumbadinha",
        amostra_ideal="Caranguejo/Casulo",
        tamanho_minimo_cm=20,
        epoca_pesca=[9, 10, 11, 12],
        melhor_hora_dia=[(0, 4), (20, 24)],
        condicoes_vento_ideais=(5.0, 20.0),
        fase_mare_ideal="enchente",
        condicoes_ondulacao_ideal=(0.3, 1.0),
        tipo_agua="Praia arenosa / Estuário",
        profundidade_ideal=2.0,
        temperatura_da_agua=(14.0, 22.0),
        fase_lunar="qualquer"
    ),
    "sargo": Peixe(
        nome="Sargo",
        nome_cientifico="Diplodus sargus",
        habitat="Zonas costeiras rochosas, sargaços e buracos em fendas",
        tecnica="Pesca à Boia / Chumbadinha",
        amostra_ideal="Camarão vivo/cozido, Mexilhão, Coreano, Percebes",
        tamanho_minimo_cm=23,
        epoca_pesca=[4, 5, 6, 7, 8, 9],
        melhor_hora_dia=[(7, 11)],
        condicoes_vento_ideais=(0.0, 15.0),
        fase_mare_ideal="enchente",
        condicoes_ondulacao_ideal=(0.2, 0.8),
        tipo_agua="Rochoso",
        profundidade_ideal=5.0,
        temperatura_da_agua=(15.0, 22.0),
        fase_lunar="qualquer"
    ),
    "corvina": Peixe(
        nome="Corvina",
        nome_cientifico="Argyrosomus regius",
        habitat="Estuários e embocaduras de rios",
        tecnica="Surfcasting pesado / Spinning com jigs",
        amostra_ideal="Choco, Lula, Isco vivo",
        tamanho_minimo_cm=45,
        epoca_pesca=[6, 7, 8, 9, 10],
        melhor_hora_dia=[(21, 24), (0, 3)],
        condicoes_vento_ideais=(5.0, 20.0),
        fase_mare_ideal="enchente",
        condicoes_ondulacao_ideal=(0.3, 1.2),
        tipo_agua="Estuário / Embocadura",
        profundidade_ideal=6.0,
        temperatura_da_agua=(16.0, 23.0),
        fase_lunar="cheia ou nova"
    ),
    "pargo": Peixe(
        nome="Pargo",
        nome_cientifico="Pagrus pagrus",
        habitat="Fundos rochosos profundos, ao largo",
        tecnica="Pesca de fundo em barco / Jigging",
        amostra_ideal="Sardinha, Lula",
        tamanho_minimo_cm=25,
        epoca_pesca=[4, 5, 6, 7, 8],
        melhor_hora_dia=[(6, 9)],
        condicoes_vento_ideais=(0.0, 15.0),
        fase_mare_ideal="qualquer",
        condicoes_ondulacao_ideal=(0.1, 0.6),
        tipo_agua="Mar aberto / Rochoso profundo",
        profundidade_ideal=35.0,
        temperatura_da_agua=(16.0, 20.0),
        fase_lunar="qualquer"
    ),
    "tainha": Peixe(
        nome="Tainha",
        nome_cientifico="Mugil cephalus",
        habitat="Estuários, docas, águas calmas costeiras",
        tecnica="Pesca com boia / isco vegetal",
        amostra_ideal="Pão, Minhoca",
        tamanho_minimo_cm=20,
        epoca_pesca=[10, 11, 12, 1, 2],
        melhor_hora_dia=[(9, 17)],
        condicoes_vento_ideais=(0.0, 12.0),
        fase_mare_ideal="qualquer",
        condicoes_ondulacao_ideal=(0.0, 0.5),
        tipo_agua="Estuário / Porto",
        profundidade_ideal=1.5,
        temperatura_da_agua=(10.0, 18.0),
        fase_lunar="qualquer"
    ),
    "carapau": Peixe(
        nome="Carapau",
        nome_cientifico="Trachurus trachurus",
        habitat="Cardumes costeiros, molhes, portos",
        tecnica="Pesca à pluma / paternoster",
        amostra_ideal="Pluma artificial, Camarão",
        tamanho_minimo_cm=15,
        epoca_pesca=[6, 7, 8, 9, 10],
        melhor_hora_dia=[(18, 23)],
        condicoes_vento_ideais=(5.0, 25.0),
        fase_mare_ideal="qualquer",
        condicoes_ondulacao_ideal=(0.3, 1.0),
        tipo_agua="Mar aberto / Porto",
        profundidade_ideal=8.0,
        temperatura_da_agua=(15.0, 22.0),
        fase_lunar="qualquer"
    ),
    "linguado": Peixe(
        nome="Linguado",
        nome_cientifico="Solea solea",
        habitat="Fundos arenosos e lodosos",
        tecnica="Surfcasting fino",
        amostra_ideal="Minhoca marinha, Bibi",
        tamanho_minimo_cm=24,
        epoca_pesca=[9, 10, 11, 12, 1],
        melhor_hora_dia=[(20, 24), (0, 5)],
        condicoes_vento_ideais=(0.0, 15.0),
        fase_mare_ideal="enchente",
        condicoes_ondulacao_ideal=(0.2, 0.8),
        tipo_agua="Praia arenosa / Estuário",
        profundidade_ideal=3.0,
        temperatura_da_agua=(10.0, 18.0),
        fase_lunar="qualquer"
    ),
}


locais_dic = {
    "carcavelos" : LocalPesca(
        nome="Praia de Carcavelos",
        latitude=38.6795,
        longitude=-9.3389,
        tipo_de_agua="Praia arenosa",
        peixes_comuns=[peixes_dic["robalo"], peixes_dic["dourada"], peixes_dic["linguado"]]
    ),
    "cabo_raso" : LocalPesca(
        nome="Cabo Raso",
        latitude=38.7181,
        longitude=-9.4875,
        tipo_de_agua="Rochoso",
        peixes_comuns=[peixes_dic["sargo"], peixes_dic["robalo"], peixes_dic["pargo"]]
    ),
    "foz_do_tejo" : LocalPesca(
        nome="Foz do Tejo (Belém)",
        latitude=38.6916,
        longitude=-9.2159,
        tipo_de_agua="Estuário",
        peixes_comuns=[peixes_dic["corvina"], peixes_dic["tainha"], peixes_dic["dourada"]]
    ),
    "praia_da_rocha" : LocalPesca(
        nome="Praia da Rocha (Portimão)",
        latitude=37.1197,
        longitude=-8.5383,
        tipo_de_agua="Rochoso / Praia arenosa",
        peixes_comuns=[peixes_dic["sargo"], peixes_dic["carapau"], peixes_dic["pargo"]]
    ),
    "ria_de_aveiro" : LocalPesca(
        nome="Ria de Aveiro",
        latitude=40.6443,
        longitude=-8.6455,
        tipo_de_agua="Estuário / Ria",
        peixes_comuns=[peixes_dic["tainha"], peixes_dic["dourada"], peixes_dic["linguado"]]
    ),
    "nazare" : LocalPesca(
        nome="Nazaré (Praia do Norte)",
        latitude=39.6088,
        longitude=-9.0742,
        tipo_de_agua="Praia arenosa / Mar aberto",
        peixes_comuns=[peixes_dic["robalo"], peixes_dic["corvina"], peixes_dic["carapau"]]
    )
}