<h2 align="center"> 💻 Script de monitoramento do comércio RagnaTales 💰 </h2>
Você cadastra itens e o preço que você deseja pagar por estes itens, o script então monitora seus itens cadastrados e o menor preço existente no mercado para cada um deles, toda vez que o preço atual do item bater o preço alerta que você cadastrou, você recebe um aviso.

### Demonstração
![image](https://github.com/mavvos/RagnaTales_market/assets/142045914/cec0ff94-2df7-4742-afb7-6ba0270490e8)

<details>
  <summary><b>COMO FUNCIONA? EXPLICAÇÃO TÉCNICA</b></summary>
<br>
O script cria um headless browser via Selenium e então procura por html tag ou xpath: a barra de pesquisa, nomes e preços dos itens. Cada item cadastrado é enviado a barra de pesquisa, cada nome de primeiro item é checado para que bata com o item enviado a barra de pesquisa e o preço seja comparado pelo item correto. Existem muitos checks para se certificar que tudo está correto, a página carregou e etc.
<br><br>
O script é essencialmente um webscraper, já que não existe acesso algum a API do RagnaTales, porque o João Tales odeia a gente.
</details>

## Download
Se você é um nerd, você vai precisar de python e selenium (requirements.txt) instalados, então clone o repositório e execute o market-tales.py

Caso você seja um ser humano normal basta fazer download da versão executável do script e abri-lo, apenas.
[Download do executável aqui](https://github.com/mavvos/RagnaTales_market/releases/latest).
> IMPORTANTE: Pode haver um falso positivo para vírus, cheque o aviso em releases.

## Como utilizar
Itens são cadastrados apenas por nome, preços devem ser escritos sem divisões por pontos ou vírgulas, apenas números inteiros, exemplo:
```
Item 0: morango
Preço alerta: 1200
```
Dessa forma toda vez que o preço atual do item Morango for igual ou menor a 1200 zenys, você receberá um alerta.

Logo após ter cadastrado todos seus itens basta apertar ENTER para enviar uma linha vazia:
```
Item 0: morango
Preço alerta: 1200
Item 1: anel do mercador
Preço alerta: 10000000
Item 2: cash
Preço alerta: 1100000
Item 3:
Delay entre sessões (segundos):
Limite de avisos: 
```

Logo após isso você deverá inserir o delay, esse delay trata do tempo de carregamento entre uma pesquisa e outra, então se por exemplo meu delay for 60 segundos, vai haver um minuto de intervalo entre uma checagem de preço e outra.
> IMPORTANTE: O delay NÃO deve ser um número pequeno, porque caso isso aconteça o sistema de proteção do site poderá bloquear seu acesso pelo seu tráfego estar sendo excessivo. Números acima de 30 segundos parecem ok.

Limite de avisos é o número máximo de avisos de preço alcançado que cada item poderá ter, então se por exemplo meu limite for 3, e o item morango estiver sendo vendido por 1000, como meu preço alerta é 1200 ele irá mostrar o alerta de preço alcançado 3 vezes e então sairá da lista de pesquisa, deixando somente os outros itens que não tiveram seu preço alcançado ainda.

Como toda vez que o limite de avisos é alcançado o item é removido da pesquisa, caso o limite de avisos de todos seus itens seja alcançado o script fechará por falta de itens. Caso você queira evitar isso basta pôr números grandes no limite.

## Informações
Apesar de já ser bem útil da maneira que está, o objetivo desse script é servir de base para que você possa modifica-lo às suas necessidades, em especial os avisos de preços alcançados, por exemplo fazendo com que eles lhe enviem uma mensagem no WhatsApp toda vez o preço que você cadastrou for batido, que é exatamente isso que o [@maxweberps](https://github.com/maxweberps/ragnatales_market) fez no seu script de onde eu tirei inspiração para fazer este que você está vendo. Afinal, um grande agradecimento a ele pela ideia.

## LICENÇA
O script é disponibilizado da maneira que ele está, sem qualquer garantias presentes ou futuras; Caso você faça besteiras e/ou sofra punições por isto, o autor não se responsabiliza por quaisquer que sejam os danos; "besteiras" pode se referir mas não se limitam aos seguintes exemplo: desenvolvimento em cima do próprio script e/ou ideia, ban/block no(s) site(s) do RagnaTales por tráfego excessivo, uso indevido qualquer que sejam estes, quebra de regras do site e/ou servidor RagnaTales, etc.
Você concorda com estes termos ao utilizar, se apropriar ou desenvolver em cima de qualquer funcionalidade ou ideia expressa neste aviso, no código fonte ou LICENÇA deste software.

[A licença completa deste software pode ser encontrada aqui.](https://github.com/mavvos/RagnaTales_market/blob/main/LICENSE.txt)
