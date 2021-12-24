# HOUSE ROCKET - INSIGHTS

<p align="center"> 
<img src="https://user-images.githubusercontent.com/76838937/147371237-fffd5dc5-3366-4522-bbbc-093f0b83b576.jpg">
</p>

**Observação**: Os dados foram extraídos do site https://www.kaggle.com/harlfoxem/housesalesprediction, a House Rocket é uma empresa real e os dados presentes no dataset não representam vínculo com a empresa, toda a situação discutida aqui é para fins de estudo (desde o CEO até as perguntas de negócio).


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
    - **Falso**: O crescimento "Year of Year" é de 0,5%
- **H5: Imóveis com 3 banheiros tem um crescimento MoM de 15%**
    - **Falso**: A variação "Month of Month" varia bastante entre os meses, mas não chega a 15%
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
