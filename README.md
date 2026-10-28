# FishPredict 🎣

O FishPredict diz-te **quando vale a pena ir pescar**. Dás-lhe uma espécie e as condições do momento (temperatura da água, vento, ondulação) e ele devolve um índice de 0 a 100%: quanto mais alto, mais as condições se parecem com aquilo que o peixe gosta.

É um projeto pessoal e de estudo, feito em Python, focado na pesca desportiva em Portugal.

[![CI](https://github.com/Jo-Oliveira/pesca-app/actions/workflows/ci.yml/badge.svg)](https://github.com/Jo-Oliveira/pesca-app/actions)

## Como funciona

Cada espécie tem um **intervalo ideal** para cada variável. O robalo, por exemplo, gosta de água entre 12 °C e 20 °C. O programa faz duas coisas:

1. **Dá uma nota de 0 a 100 a cada variável.** 100 se o valor está mesmo no meio do intervalo ideal, 0 se está no limite ou fora dele. Entre os dois, a nota desce de forma proporcional.
2. **Junta as notas numa só**, com uma média ponderada: há variáveis que pesam mais do que outras para cada espécie.

### A nota de uma variável

A função `nota(valor, minimo, maximo)` usa três conceitos:

- **centro**: o ponto a meio do intervalo ideal (o melhor valor possível).
- **distância**: a que distância do centro está o valor medido.
- **raio**: a distância do centro até ao limite do intervalo, ou seja, metade da largura total.

A conta é `nota = (1 - distância / raio) × 100`, e nunca fica abaixo de 0.

Exemplo com a temperatura do robalo (ideal entre 12 °C e 20 °C, centro a 16 °C, raio de 4):

| Temperatura da água | Distância ao centro | Nota |
|---|---|---|
| 16 °C | 0 | 100 |
| 19 °C | 3 | 25 |
| 20 °C (limite) | 4 | 0 |
| 22 °C (fora) | 6 | 0 |

Se o intervalo for um único valor (mínimo igual ao máximo), a nota é 100 só se o valor for exatamente esse, e 0 caso contrário.

### Os pesos

Cada espécie tem um peso por variável (temperatura, vento, ondulação), e **os pesos têm de somar 1**. O programa recusa criar uma espécie cujos pesos não somem 1, para não dar resultados errados em silêncio.

O índice final é a soma de cada nota multiplicada pelo seu peso. Por exemplo, com notas de 25 (temperatura), 27 (vento) e 0 (ondulação) e pesos de 0.25, 0.30 e 0.45:

`25 × 0.25 + 27 × 0.30 + 0 × 0.45 = 14.35`

Os pesos que uso hoje são **valores provisórios**, escolhidos por mim. Não vêm de um estudo científico.

## Estrutura do projeto

```
src/
  models.py        # Peixe, LocalPesca e Condicoes
  databases.py     # os peixes e os locais de pesca
  recomendacao.py  # nota() e indice(): o motor de pontuação
  services.py      # ligação à API do tempo
tests/             # testes com Pytest
main.py            # exemplo de utilização
```

## Como correr

Precisas de Python 3.11 ou superior.

```bash
git clone https://github.com/Jo-Oliveira/pesca-app.git
cd pesca-app

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python main.py     # corre o exemplo
pytest             # corre os testes
```

## Qualidade do código

- Testes com **Pytest**, incluindo os casos-limite da função `nota()` (centro, limites, fora do intervalo e intervalo de um só valor).
- **Ruff** para verificar o estilo do código.
- **GitHub Actions** corre o `ruff` e o `pytest` em cada `push`.

## Estado do projeto e próximos passos

- [x] Nota por variável (`nota()`) com testes
- [x] Índice com média ponderada (`indice()`) e validação dos pesos
- [x] Pipeline de CI
- [ ] Ligar a API do tempo para usar dados reais
- [ ] Mais variáveis: pressão barométrica, maré, hora do dia
- [ ] Docker
- [ ] Interface de saída (CLI ou API)

## Limitações

- Os pesos e os intervalos ideais de cada espécie são estimativas minhas e podem estar errados.
- A fase da lua é muito usada pelos pescadores, mas a evidência científica é fraca, por isso terá um peso baixo quando for incluída.
- Por agora o índice só usa temperatura da água, vento e ondulação.
