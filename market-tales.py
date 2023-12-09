"""Script para monitoramento de itens no market do RagnaTales.
Essa é uma versão adaptada do script feito por maxweberps;
Original: https://github.com/maxweberps/ragnatales_market
"""
import re
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Constantes
XPATH_PESQUISA = (
    '//*[@id="app"]/div/div/div[2]/div/div[2]/div[1]/label/div/div[1]/input'
)
XPATH_PRECO_ATUAL = '//*[@id="app"]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[3]/div/span'


def main():
    # Cadastro de itens
    count = 0
    itens_monitorados = {}
    print("--- CADASTRO DE MONITORAMENTO DE ITENS ---")
    while True:
        item = input(f"Item {count}: ")
        if item == "":
            break
        else:
            count += 1
            item = item.title()
            preco_alerta = int(input("Preço a alertar: "))
            itens_monitorados[item] = [preco_alerta, 1003000700, 0]
    DELAY = int(input("Delay entre sessões (segundos): "))
    LIMITE_AVISOS = int(input("Limite de avisos: "))

    # Browser
    nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    sessao = 1
    nav.get("https://ragnatales.com.br/market")
    time.sleep(5)

    # Loop de monitoramento
    while True:
        if len(itens_monitorados) == 0:
            print("Não há itens para monitorar.")
            time.sleep(4)
            sys.exit(1)

        print(f"----- SESSÃO DE PESQUISA Nº {sessao} -----")
        for item in itens_monitorados:
            if itens_monitorados[item][2] == LIMITE_AVISOS:
                itens_monitorados.pop(item)
                print(f"Limite de avisos de {item} alcançado, item removido da lista.")
                break

            time.sleep(2)
            try:
                nav.find_element(
                    "xpath",
                    XPATH_PESQUISA,
                ).clear()

                nav.find_element(
                    "xpath",
                    XPATH_PESQUISA,
                ).send_keys(item)

                nav.find_element(
                    "xpath",
                    XPATH_PESQUISA,
                ).send_keys(Keys.ENTER)
                time.sleep(3)
            except Exception as e:
                print("> Página não carregada, conexão instável.")
                break

            try:
                preco_atual = convert(
                    nav.find_element(
                        "xpath",
                        XPATH_PRECO_ATUAL,
                    ).text
                )
                itens_monitorados[item][1] = preco_atual
            except Exception as e:
                print(f"> Nenhum registro encontrado do item {item}.")
                itens_monitorados[item][1] = 1003000700

            if itens_monitorados[item][1] != 1003000700:
                print(
                    f"> {item} - Preço atual: {itens_monitorados[item][1]}z || Alerta: {itens_monitorados[item][0]}z"
                )

                if itens_monitorados[item][0] >= itens_monitorados[item][1]:
                    print(f"> Preço alerta do item {item} alcançado!!!")
                    itens_monitorados[item][2] += 1  # Adiciona ao limite de avisos
                else:
                    print(f"> Preço alerta do item {item} não alcançado.")

        nav.refresh()
        nav.implicitly_wait(DELAY)
        time.sleep(DELAY)
        sessao += 1


def convert(preco_str):
    numeros = re.findall(r"\d+", preco_str)
    num = "".join(numeros)
    return int(num)


if __name__ == "__main__":
    main()
