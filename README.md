# HOUSE ROCKET - INSIGHTS

<p align="center"> 
<img src="https://user-images.githubusercontent.com/76838937/147371237-fffd5dc5-3366-4522-bbbc-093f0b83b576.jpg">
</p>

**Observação**: Os dados foram extraídos do site https://www.kaggle.com/harlfoxem/housesalesprediction, a House Rocket é uma empresa real e os dados presentes no dataset não representam vínculo com a empresa, toda a situação discutida aqui é para fins de estudo (desde o CEO até as perguntas de negócio). Ao final do projeto os dados foram apresentados em um Dashboard feito no Qlik Sense.

**Acesso ao Projeto**: Caso deseje acessar o projeto completo basta clicar aqui --> [Insights - House Rocket](https://github.com/Mat004/Insights-House-Rocket/blob/main/Insights%20-%20House%20Rocket.ipynb)

**Acesso ao Dashboard no Heroku**: [Heroku App](https://app-house-rocket-insight.herokuapp.com/)


# Sobre a House Rocket

A House Rocket é uma plataforma digital que tem como modelo de negócio, a compra e a venda de imóveis usando tecnologia. Sua principal estratégia é comprar boas casas em ótimas localizações com preços baixos e depois revendê-las posteriormente à preços mais altos. Quanto maior a diferença entre a compra e a venda, maior o lucro da empresa e portanto maior sua receita.
Entretanto, as casas possuem muitos atributos que as tornam mais ou menos atrativas aos compradores e vendedores e a localização e o período do ano também podem influenciar os preços.


# Problemas de Negócio

O CEO da House Rocket deseja que a principal estratégia da empresa seja de comprar bons imóveis, em localizações boas, para depois revendê-las posteriormente a um valor superior ao de compra. O lucro será proporcional a diferença entre o preço de venda e o preço de compra do imóvel, quanto maior essa diferença, maior será o lucro. Os questionamentos do CEO foram:

1. Quais são os imóveis que a House Rocket deve comprar?
2. Uma vez o imóvel comprado, qual o melhor preço para vendê-los?


# Planejamento da Solução

Com os dados extraídos e feito o tratamento de dados, com uma descrição básica dos dados já podemos compreender melhor a forma como estão distribuídos:

<p align="center"> 
<img src="https://user-images.githubusercontent.com/76838937/147372098-fda0b167-95e6-443a-81a9-6298f3f57df3.png">
</p>

Com essas informações podemos observar que o imóvel com o menor preço custa $75 mil dólares enquanto o mais caro custa $7,7 milhões de dólares, a média dos preços é de $540 mil dólares e a mediana com $450 mil dólares. Ao apresentar essas informações ao CEO, ele estimou a compra de imóveis que estivessem com o preço abaixo da mediana, isso agrupando por região tendo em vista que o preço pode sofrer variação pela região.


# Hipóteses 

- **H1: Imóveis com vista para a água são 30% mais caros, na média**
    - **Falso**: Imóveis com vista para a água são 212% mais caros    
- **H2: Imóveis com data de construção menor que 1955 são 50% mais baratos, na média**
    - **False** : Os imóveis com data de construção inferior a 1955 são, aproximadamente, 2% mais baratos
- **H3: Imóveis sem porão são 50% maiores que com porão**
    - **Falso**: Imóveis sem porão são, aproximadamente, 23% mais baratos
- **H4: O crescimento do preço dos imóveis YoY é de 10%**
    - **Falso**: O crescimento "Year over Year" é de 0,5%
- **H5: Imóveis com 3 banheiros tem um crescimento MoM de 15%**
    - **Falso**: A variação "Month over Month" varia bastante entre os meses, mas não chega a 15%
- **H6: A maioria dos imóveis com vista para a água possuem estado de conservação "good"**
    - **Falso**: A grande maioria possui estado de conservação "regular"
- **H7: Imóveis mais novos possuem preço médio maior**
    - **Verdadeiro**: Imóveis mais novos são 18% mais caros que os antigos
- **H8: Imóveis com 2 andares possuem preço médio maior que a mediana**
    - **Verdadeiro**: Imóveis com 2 andares possuem maior quantidade e possuem preço médio maior que a mediana
- **H9: Imóvel antigo com reforma feita, são mais caros que aqueles sem reforma**
    - **Verdadeiro**: Imóveis antigos já reformados, são 50% mais caros que os imóveis sem reforma
- **H10: A maioria dos imóveis do tipo "apartament" possuem estado de conservação "good"**
    - **Falso**: A grande parte dos imóveis do tipo "apartament" possuem estado de conservação "regular"
 
 
 # Resultados
 
- Quais são os imóveis que a House Rocket deve comprar?
    - Imóveis com preço abaixo da mediana da região 
    - Imóveis em condições "regular" e "good"
    - A quantidade total de imóveis é de 21.613 e quantidade classificada para compra é de 10.579
- Uma vez o imóvel comprado, qual o melhor preço para vendê-los?
    - Se o preço de compra do imóvel for maior que a mediana da região, o preço da venda será o preço da compra com acréscimo de 10%
    - Se o preço de compra do imóvel for menor que a mediana da região, o preço da venda será o preço da compra com acréscimo de 30%
- Investimento
    - Caso haja a compra dos imóveis classificados para venda, o valor investido será de $4,1 bilhões de dólares
    - Com a venda de todos os imóveis, a receita estimada é de $5,3 bilhões de dólares
    - O lucro final será de $1,2 bilhões de dólares

**_Mapa com os imóveis_**
- Em boas condições (good)

<p align="center"> 
<img src="https://user-images.githubusercontent.com/76838937/147372816-0092089b-871f-4e52-80dc-2612f3d70883.png">
</p>

- Em condições regulares (regular)

<p align="center"> 
<img src="https://user-images.githubusercontent.com/76838937/147372819-16315474-51d8-468f-aac1-5fabbdab6515.png">
</p>

- Em condições ruins (bad)

<p align="center"> 
<img src="https://user-images.githubusercontent.com/76838937/147372824-60c710cd-f460-480c-a011-728b62c9fd94.png">
</p>



# Dashboard 

**_Resumo_**
![WhatsApp Image 2022-01-15 at 1 14 28 PM](https://user-images.githubusercontent.com/76838937/149629192-155c505d-c59a-46f5-9fc6-3ebda523e259.jpeg)


**_Descriminado_**
![WhatsApp Image 2022-01-15 at 1 14 55 PM](https://user-images.githubusercontent.com/76838937/149629258-d3a6eab2-8d5c-41bf-8ff6-e1ab6a716b2f.jpeg)


**_Mapa_**
![WhatsApp Image 2022-01-15 at 1 15 59 PM](https://user-images.githubusercontent.com/76838937/149629285-a3216e12-7fa3-4f7d-889a-5c631497d1d7.jpeg)


**_Tabela_**
![WhatsApp Image 2022-01-15 at 1 16 35 PM](https://user-images.githubusercontent.com/76838937/149629316-66a1e3be-7964-460b-ac88-942bed36dce3.jpeg)


## Vídeo
https://user-images.githubusercontent.com/76838937/149628932-51d88abd-6d49-4c89-9a09-aecfe6c618cd.mp4
