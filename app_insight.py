#App Heroku

from PIL import Image
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
import geopandas
import folium



# ------------------------------------------
# settings
# ------------------------------------------
st.set_page_config( layout='wide' )


# ------------------------------------------
# Welcome
# ------------------------------------------

st.title('House Rocket Dashboard')

st.markdown('---')
st.markdown('## Sobre a base de dados')
st.markdown('''Os dados analisados foram extraídos do Kaggle, a House Rocket é uma empresa real sendo uma plataforma digital
            que tem como modelo de negócio, a compra e a venda de imóveis usando tecnologia. Os dados presentes no dataset não
            representam vínculo com a empresa, toda a situação discutida aqui é para fins de estudo (desde o CEO até as perguntas de negócio).
            ''')
st.markdown('\n''''*Dicionário dos dados*:''')
st.markdown("- id: Notação para cada imóvel"
            '\n'"- date: Data de venda da imóvel"
            '\n'"- price: Preço de venda da imóvel"
            '\n'"- bedrooms: Número de quartos"
            '\n'"- bathrooms: Número de banheiros"
            '\n'"- sqft_living: Metragem quadrada da sala de estar"
            '\n'"- sqrt_log: Metragem quadrada do lote"
            '\n'"- floors: Quantidade de andares"
            '\n'"- waterfront: Vista para a água"
            '\n'"- view: Foi visualizado"
            '\n'"- condition: Condição do imóvel"
            '\n'"- grade: Nota geral dada à unidade habitacional"
            '\n'"- sqft_above: Metragem quadrada do imóvel"
            '\n'"- sqft_basement: Metragem quadrada do porão"
            '\n'"- yr_built: Ano de construção"
            '\n'"- yr_renovated: Ano em que o imóvel foi reformado"
            '\n'"- zipcode: Código postal"
            '\n'"- lat: Latitude"
            '\n'"- long: Longitude"
            '\n'"- sqft_living15: Metragem quadrada da sala de estar em 2015 (implica em algumas renovações)"
            '\n'"- sqrt_lot15: Metragem quadrada do lote em 2015 (implica em algumas renovações)"
            '\n'"- dormitory_type: Classificação do imóvel baseado na quantidade de quartos"
            '\n'"- condition_type: Classificação da condição de conversação do imóvel"
            '\n'"- size: Classificação do tamanho do imóvel baseado no tamanho da sala de estar"
            '\n'"- is_renovated: Se o imóvel foi reformado ou não"
            '\n'"- is_waterfront: Se o imóvel possui vista para a água"
            '\n'"- house_age: Classificação do imóvel se é antigo (old) ou novo (new)"
            '\n'"- yr_date: Ano da data de venda do imóvel"
            '\n'"- month_date: Mês da data de venda do imóvel"
            )
st.markdown('---')


# ------------------------------------------
# helper functions
# ------------------------------------------

@st.cache(allow_output_mutation=True)
def get_geofile(url):
    geofile = geopandas.read_file(url)

    return geofile

@st.cache(allow_output_mutation=True)
def get_data(path):
    
    data = pd.read_csv(path)
    
    return data

def describe(data):
    
    num_attributes = data.select_dtypes( include=['int64', 'float64'] )
    media = pd.DataFrame( num_attributes.apply( np.mean ) )
    mediana = pd.DataFrame( num_attributes.apply( np.median ) )
    std = pd.DataFrame( num_attributes.apply( np.std ) )

    max_ = pd.DataFrame( num_attributes.apply( np.max ) ) 
    min_ = pd.DataFrame( num_attributes.apply( np.min ) ) 

    df_sc = pd.concat([max_, min_, media, mediana, std], axis=1 ).reset_index()
    df_sc.columns = ['attributes', 'max', 'min', 'mean', 'median', 'std']

    st.title('\n''Data Describe')
    st.write(df_sc)

# -----------------------------------------
# Main functions
# -----------------------------------------

def data_overview( data ):

    image = Image.open('HR.png')
    st.sidebar.image(image, caption='House Rocket', use_column_width=True)

    st.sidebar.title('Data overview')

    f_attributes = st.sidebar.multiselect( 'Enter columns', data.columns ) 
    f_zipcode = st.sidebar.multiselect( 'Enter zipcode', data['zipcode'].unique() )

    st.title('Data Overview')

    if (f_zipcode != []) & (f_attributes != []):
        data = data.loc[data['zipcode'].isin(f_zipcode), f_attributes]

    elif (f_zipcode != []) & (f_attributes == []):
        data = data.loc[data['zipcode'].isin(f_zipcode), :]

    elif (f_zipcode == []) & (f_attributes != []):
        data = data.loc[:, f_attributes]

    else:
        data = data.copy()

    st.write(data.head(10))


def hypotheses_def(data):
    st.markdown('---')
    st.markdown('# Hyphoteses')

    sd = st.selectbox(
    "Select Hyphoteses",
        ["Hipótese 1", "Hipótese 2", "Hipótese 3", "Hipótese 4",
         "Hipótese 5", "Hipótese 6", "Hipótese 7", "Hipótese 8",
         "Hipótese 9", "Hipótese 10"]


    )

    if sd == "Hipótese 1":
        st.markdown('### Hipótese 1: Imóveis com vista para a água são 30% mais caros, na média')
        st.markdown('''- Falso: Imóveis com vista para a água são 212% mais caros''')
        df1 = data.groupby('is_waterfront')['price'].mean().reset_index()
        df1['%'] = df1['price'].pct_change()
        porcen = (df1['%'][1]) * 100

        fig1 = px.bar(df1, 'is_waterfront', 'price')
        st.plotly_chart(fig1, use_container_width=True)

        st.markdown('\n'f'##### Imóveis com vista para a água são {porcen:.2f}% mais caros que os imóveis sem vista.')

    elif sd == "Hipótese 2":
        st.markdown('### Hipótese 2: Imóveis com data de construção menor que 1955 são 50% mais baratos, na média')
        st.markdown('''- Falso: Os imóveis com data de construção inferior a 1955 são, aproximadamente, 2% mais baratos''')
        df2 = data.copy()
        df2['yr_built_analysis'] = df2['yr_built'].apply(lambda x: '<= 1955' if x <= 1955 else '> 1955')
        df2_aux = df2.groupby('yr_built_analysis')['price'].mean().reset_index()
        df2_aux['%'] = df2_aux['price'].pct_change()
        porcen_df2 = (df2_aux['%'][1]) * 100
        df2_m = df2[df2['yr_built_analysis'] == '<= 1955']
        df2_p = df2[df2['yr_built_analysis'] == '> 1955']
        c1, c2 = st.columns(2)

        fig2 = px.bar(df2, 'yr_built_analysis', 'price', color='yr_built_analysis')
        c1.plotly_chart(fig2, use_containder_width=True)

        fig3 = px.histogram(df2, 'price', color='yr_built_analysis')
        c2.plotly_chart(fig3, user_containder_width=True)

        st.markdown(f'##### A quantidade de imóveis com ano até 1955: {len(df2_m)}')
        st.markdown(f'##### A quantidade de imóveis com ano de constução acima de 1955: {len(df2_p)}')
        st.markdown('\n'f' ##### Os imóveis com ano de construção menor que 1955 possuem valor {porcen_df2:.2f}% menor que os imóveis acima desse ano.')


    elif sd == "Hipótese 3":
        st.markdown('### Hipótese 3: Imóveis sem porão são 50% maiores que com porão')
        st.markdown('''- Imóveis sem porão são, aproximadamente, 23% mais baratos''')
        df3 = data.copy()
        df3['basement'] = df3['sqft_basement'].apply(lambda x: 'without_basement' if x == 0 else 'with_basement')
        no_basement = data.loc[data['sqft_basement'] == 0, 'sqft_above'].mean()
        with_basement = data.loc[data['sqft_basement'] > 0, 'sqft_above'].mean()
        dif = ((no_basement / with_basement) - 1) * 100

        c3, c4 = st.columns(2)

        fig4 = px.bar(df3, 'basement', 'price')
        c3.plotly_chart(fig4, user_containder_width=True)

        fig5 = px.histogram(df3, 'price', color='basement')
        c4.plotly_chart(fig5, user_containder_width=True)

        st.markdown(f'##### A média do tamanho do imóvel sem porão é de: {no_basement:.2f}')
        st.markdown(f'##### A média do tamanho do imóvel com porão é de: {with_basement:.2f}')
        st.markdown('\n'f'##### Imóveis sem porão são {dif:.2f}% maiores que imóveis com porão.')

    elif sd == "Hipótese 4":
        st.markdown('### Hipótese 4: O crescimento do preço dos imóveis YoY é de 10%')
        st.markdown('''- Falso: O crescimento "Year of Year" é de 0,5%''')
        df4 = data.groupby('yr_date')['price'].mean().reset_index()
        df4['%'] = df4['price'].pct_change()
        dif_df4 = (df4['%'][1]) * 100

        fig6 = px.bar(df4, 'yr_date', 'price')
        st.plotly_chart(fig6, use_container_width=True)

        st.markdown('\n'f'##### O crescimento do preço dos imóveis YoY é de {dif_df4:.2f}%')

    elif sd == "Hipótese 5":
        st.markdown('### Hipótese 5: Imóveis com 3 banheiros tem um crescimento MoM de 15%')
        st.markdown('''- Falso: A variação "Month of Month" varia bastante entre os meses, mas não chega a 15%''')
        df5 = data.loc[data['bathrooms'] == 3]
        df5_aux = df5.groupby('month_date')['price'].mean().reset_index()
        df5_aux['%'] = df5_aux['price'].pct_change()
        df5_aux['color'] = df5_aux['%'].apply(lambda x: 'negative' if x < 0 else 'positive')

        fig7 = px.bar(df5_aux, 'month_date', '%', color='color')
        st.plotly_chart(fig7, use_container_width=True)

    elif sd == "Hipótese 6":
        st.markdown('### Hipótese 6: A maioria dos imóveis com vista para a água possuem estado de conservação "good"')
        st.markdown('''- Falso: A grande maioria possui estado de conservação "regular"''')
        df6 = data.loc[data['is_waterfront'] == 'yes']
        df6 = df6.groupby('condition_type')['id'].count().reset_index()
        lista_id = list(df6['id'])

        fig8 = px.bar(df6, 'id', 'condition_type', color='condition_type')
        st.plotly_chart(fig8, use_container_width=True)

        st.markdown(f'##### A quantidade de imóveis na condição "bad" é de {lista_id[0]}')
        st.markdown(f'##### A quantidade de imóveis na condição "good" é de {lista_id[1]}')
        st.markdown(f'##### A quantidade de imóveis na condição "regular" é de {lista_id[2]}''\n')

    elif sd == "Hipótese 7":
        st.markdown('### Hipótese 7: Imóveis mais novos possuem preço médio maior')
        st.markdown('''- Verdadeiro: Imóveis mais novos são 18% mais caros que os antigos''')
        df_h7 = data.copy()
        df_h7_aux = df_h7.groupby('house_age')['id'].count().reset_index()
        df_h7_aux2 = df_h7.groupby('house_age')['price'].mean().reset_index()

        c5, c6 = st.columns(2)

        fig9 = px.bar(df_h7_aux, 'house_age', 'id', color='house_age')
        c5.plotly_chart(fig9, user_containder_width=True)

        fig10 = px.bar(df_h7_aux2, 'house_age', 'price', color='house_age')
        c6.plotly_chart(fig10, use_container_width=True)

        new = len(data.loc[data['house_age'] == 'new'])
        old = len(data.loc[data['house_age'] == 'old'])
        new_mean = data.loc[data['house_age'] == 'new', 'price'].mean()
        old_mean = data.loc[data['house_age'] == 'old', 'price'].mean()

        st.markdown(f'##### A quantidade de imóveis "new" é {new} e média dos preços é {new_mean:.2f}')
        st.markdown(f'##### A quantidade de imóveis "old" é {old} e a média dos preços é {old_mean:.2f}')
        st.markdown(f'##### Os imóveis novos são {((new_mean / old_mean) - 1) * 100:.2f}% mais caros que os antigos''\n')

    elif sd == "Hipótese 8":
        st.markdown('### Hipótese 8: Imóveis com 2 andares possuem preço médio maior que a medianar')
        st.markdown('''- Verdadeiro: Imóveis com 2 andares possuem maior quantidade e possuem preço médio maior que a mediana''')
        df8 = data.loc[data['floors'] == 2]
        df8_median = np.median(df8['price'])
        df8_mean = np.mean(df8['price'])

        fig11 = px.strip(data, 'floors', 'price', color='floors')
        st.plotly_chart(fig11, use_container_width=True)

        st.markdown(f'##### Quantidade de imóveis com 2 andares: {len(df8)}')
        st.markdown('\n'f' ##### A mediana dos preços de imóveis com 2 andares: {df8_median:.2f}')
        st.markdown(f'##### A média dos preços de imóveis com 2 andares: {df8_mean:.2f}''\n')

    elif sd == "Hipótese 9":
        st.markdown('### Hipótese 9: Imóvel antigo com reforma feita, são mais caros que aqueles sem reforma')
        st.markdown('''- Verdadeiro: Imóveis antigos já reformados, são 50% mais caros que os imóveis sem reforma''')

        df9 = data.loc[(data['house_age'] == 'old')]
        df9_aux = df9.groupby('is_renovated')['price'].mean().reset_index()
        df9_aux['%'] = df9_aux['price'].pct_change()

        porc_df9 = (df9_aux['%'][1]) * 100
        cont_1 = len(df9.loc[(df9['is_waterfront'] == 'yes')])
        cont_2 = len(df9.loc[(df9['is_waterfront'] == 'yes') & (df9['is_renovated'] == 'renovated')])

        fig12 = px.bar(df9, 'is_renovated', 'price', color='is_renovated')
        st.plotly_chart(fig12, use_container_width=True)

        st.markdown(f'##### Quantidade de imóveis antigos e que possuem vista para a água: {cont_1}')
        st.markdown(f'##### Quantidade de imóveis antigos reformados com vista para a água: {cont_2}')
        st.markdown('\n'f'##### Imóveis antigos com reforma, são {porc_df9:.2f}% mais caros que aqueles sem reforma.''\n')

    elif sd == "Hipótese 10":
        st.markdown('### Hipótese 10: A maioria dos imóveis do tipo "apartament" possuem estado de conservação "good" ')
        st.markdown('''- Falso: A grande parte dos imóveis do tipo "apartament" possuem estado de conservação "regular"''')

        df10 = data.loc[data['domitory_type'] == 'apartament']
        df10_aux = df10.groupby('condition_type')['id'].count().reset_index()

        df10_count = list(df10_aux['id'])

        c7, c8 = st.columns(2)

        fig13 = px.bar(df10, 'condition_type', 'price', color='condition_type')
        c7.plotly_chart(fig13, use_container_width=True)

        fig14 = px.histogram(df10, 'price', color='condition_type')
        c8.plotly_chart(fig14, use_container_width=True)

        st.markdown('\n'f'##### A quantidade de imóveis do tipo "apartament" em condições "bad": {df10_count[0]}')
        st.markdown(f'##### A quantidade de imóveis do tipo "apartament" em condições "regular": {df10_count[1]}')
        st.markdown(f'##### A quantidade de imóveis do tipo "apartament" em condições "good": {df10_count[2]}''\n')

    #st.markdown('---')

    return None

def ceo_questions(data):

    st.markdown('---')
    st.markdown('# CEO questions')
    st.markdown('### - Quais são os imóveis que a House Rocket deve comprar?')
    st.markdown('### - Uma vez o imóvel comprado, qual o melhor preço para vendê-los?')
    st.markdown('''- Regras para compra: Imóveis com preço abaixo da mediana da região e Tenha condição "regular" ou "good"''')
    st.markdown('''- Regras para venda: Se o preço de compra for maior que a mediana da região, o preço de venda será o preço de compra + 10%,
    se o preço de compra for menor que a mediana da região, o preço de venda será o preço de compra + 30%''')
    st.markdown('---')

    # Quantidade de imóveis
    dt1 = data[data['purchase'] == 'buy']

    st.markdown(f'##### Quantidade de imóveis disponível: {len(data)}')
    st. markdown(f'##### Quantidade de imóveis classificados para a compra: {len(dt1)}')

    # Resumo dos principais resultados
    dt2 = dt1['price'].sum()
    dt3 = data.loc[data['purchase'] == 'buy', 'sales_price'].sum()

    st.markdown(f'##### Total do investimento caso haja a compra de todos os imóveis classificados para compra: ${dt2:.2f}')
    st.markdown(f'##### O valor da venda dos imóveis classificados: ${dt3:.2f}')
    st.markdown(f'##### O lucro obtido pela venda desses imóveis: ${(dt3 - dt2):.2f}')

    return None

def ceo_map(data, geofile):
    c1, c2 = st.columns((1, 1))

    density_map = folium.Map(location=[data['lat'].mean(), data['long'].mean()],
                              default_zoom_start=15)

    marker_cluster = MarkerCluster().add_to(density_map)
    for name, row in data.iterrows():
        folium.Marker([row['lat'], row['long']],
            popup='Sold R${0} on: {1}. Features: {2} sqft, {3} bedrooms, {4} bathrooms, year built: {5}, purchase: {6}'.format(row['price'],
                           row['date'],
                           row['sqft_living'],
                           row['bedrooms'],
                           row['bathrooms'],
                           row['yr_built'],
                           row['purchase'])).add_to(marker_cluster)


    with c1:
        folium_static( density_map )


    df = data[['price', 'zipcode']].groupby( 'zipcode' ).mean().reset_index()
    df.columns = ['ZIP', 'PRICE']

    geofile = geofile[geofile['ZIP'].isin(df['ZIP'].tolist())]

    region_price_map = folium.Map(location=[data['lat'].mean(),
                                   data['long'].mean()],
                                   default_zoom_start=15)


    region_price_map.choropleth(data = df,
                                 geo_data = geofile,
                                 columns=['ZIP', 'PRICE'],
                                 key_on='feature.properties.ZIP',
                                 fill_color='YlOrRd',
                                 fill_opacity = 0.7,
                                 line_opacity = 0.2,
                                 legend_name='AVG PRICE')
    with c2:
        folium_static(region_price_map)

    return None

if __name__ == "__main__":
    # ETL
    path = 'kc_house_data_report.csv'
    url = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'
    geofile = get_geofile(url)

    # load data
    data = get_data(path)
    data_overview(data)
    describe(data)

    # transformation
    hypotheses_def(data)
    ceo_questions(data)
    ceo_map(data, geofile)
