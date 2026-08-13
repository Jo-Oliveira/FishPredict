from src.models import Peixe

peixes_dic = {
   "robalo" : Peixe(
    nome="Robalo",
    nome_cientifico="Dicentrarchus labrax",
    habitat="Rebentação / Zonas de rocha e areia",
    tecnica="Spinning",
    amostra_ideal="Amostra rija / Vinil",
    tamanho_minimo_cm=42
), "dourada" : Peixe(
        nome = "Dourada",
        nome_cientifico = "Sparus aurata",
        habitat = "Fundos de areia, lodo, estuários e rias",
        tecnica = "Surfcasting / Chumbadinha",
        amostra_ideal = "Caranguejo/Casulo",
        tamanho_minimo_cm = 19
), "sargo" : Peixe(
        nome = "Sargo",
        nome_cientifico = "Diplodus sargus",
        habitat = "Zonas costeiras rochosas, sargaços e buracos em fendas",
        tecnica = "Pesca à Boia / Chumbadinha",
        amostra_ideal = "Camarão vivo/cozido, Mexilhão, Coreano, Percebes",
        tamanho_minimo_cm = 15
    )


}


