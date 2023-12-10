"""Script para monitoramento de itens no market do RagnaTales.
Essa é uma versão adaptada do script feito por maxweberps;
Original: https://github.com/maxweberps/ragnatales_market
"""
import re
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PRECO_MAX = 1003000700


def cli():
    """Interface de cadastro de itens"""
    count = 0
    itens_monitorados = {}
    print("-- CADASTRO DE MONITORAMENTO DE ITENS --")
    while True:
        item = input(f"Item {count}: ")
        if item == "":
            break
        else:
            count += 1
            item = item.title()
            preco_alerta = int(input("Preço a alertar: "))
            itens_monitorados[item] = [preco_alerta, PRECO_MAX, 0]
    DELAY = int(input("Delay entre sessões (segundos): "))
    LIMITE_AVISOS = int(input("Limite de avisos: "))
    return itens_monitorados, DELAY, LIMITE_AVISOS


def main():
    """Função principal"""
    itens_monitorados, DELAY, LIMITE_AVISOS = cli()
    MAX_ESPERA = 10  # Tempo de espera máximo para carregar páginas e preços
    XPATH_PRECO_ATUAL = '//*[@id="app"]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[3]/div/span'

    # Browser
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Navegador sem interface
    nav = webdriver.Chrome(options=options)
    nav.get("https://ragnatales.com.br/market")
    sessao = 1

    # Loop de monitoramento
    while True:
        if not itens_monitorados:
            print("Não há itens para monitorar.")
            time.sleep(4)
            nav.quit()
            sys.exit(1)

        print(f"------- SESSÃO DE PESQUISA Nº {sessao} -------")
        for item in itens_monitorados:
            if itens_monitorados[item][2] >= LIMITE_AVISOS:
                itens_monitorados.pop(item)
                print(f"Limite de avisos de {item} alcançado, item removido da lista.")
                break

            try:
                pesquisa = WebDriverWait(nav, MAX_ESPERA).until(
                    EC.presence_of_element_located((By.TAG_NAME, "input"))
                )
                time.sleep(1)
                pesquisa.clear()
                pesquisa.send_keys(item)
                pesquisa.send_keys(Keys.ENTER)
                time.sleep(3)
            except Exception as e:
                print("> Página não carregada, conexão instável.")
                break

            try:
                preco_atual = WebDriverWait(nav, MAX_ESPERA).until(
                    EC.presence_of_element_located((By.XPATH, XPATH_PRECO_ATUAL))
                )
                itens_monitorados[item][1] = convert(preco_atual.text)
            except Exception as e:
                print(f"> Nenhum registro encontrado do item {item}.")
                itens_monitorados[item][1] = PRECO_MAX

            if itens_monitorados[item][1] != PRECO_MAX:
                print(
                    f"> {item} - Preço atual: {itens_monitorados[item][1]}z || Alerta: {itens_monitorados[item][0]}z"
                )

                if itens_monitorados[item][0] >= itens_monitorados[item][1]:
                    print(f"> Preço alerta do item {item} alcançado!!!")
                    itens_monitorados[item][2] += 1  # Adiciona ao limite de avisos
                else:
                    print(f"> Preço alerta do item {item} não alcançado.")

        time.sleep(DELAY)
        sessao += 1


def convert(preco_str):
    """Converte zeny STR para INT"""
    numeros = re.findall(r"\d+", preco_str)
    num = "".join(numeros)
    return int(num)


if __name__ == "__main__":
    main()
