import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
c1, c2, c3, c4 = st.beta_columns((2, 1, 1, 1))
# header = st.beta_container()
# dataset = st.beta_container()
# features = st.beta_container()

casa_dos_dados = pd.read_csv("casa_dos_dados_finais2.csv")
recomendacao = pd.read_csv("data_recomendacao.csv")
relacoes = pd.read_csv("data_relacoes2.csv")
relacoes_unicas = pd.read_csv("data_relacoes_agg.csv")
perfis = pd.read_csv("perfis_cluster7.csv")

recomendacaot = pd.read_csv("recomendacaot.csv")


with c1:
    
    st.title("Projeto de Recomendação")
    st.text("Dashboard de teste de funcionamento")

    empresa = st.selectbox('Escolha uma empresa', casa_dos_dados['empresa_buscada'])

    cnpj = casa_dos_dados[casa_dos_dados['empresa_buscada'] == empresa]['cnpj'].values[0]
    razao_social = casa_dos_dados[casa_dos_dados['empresa_buscada'] == empresa]['razao_social'].values[0]
    data_abertura = casa_dos_dados[casa_dos_dados['empresa_buscada'] == empresa]['data_abertura'].values[0]
    situacao_cadastral = casa_dos_dados[casa_dos_dados['empresa_buscada'] == empresa]['situacao_cadastral'].values[0]
    capital_social = casa_dos_dados[casa_dos_dados['empresa_buscada'] == empresa]['capital_social'].values[0]
    natureza_juridica = casa_dos_dados[casa_dos_dados['empresa_buscada'] == empresa]['natureza_juridica'].values[0]
    municipio = casa_dos_dados[casa_dos_dados['empresa_buscada'] == empresa]['municipio'].values[0]
    uf = casa_dos_dados[casa_dos_dados['empresa_buscada'] == empresa]['uf'].values[0]
    atividade = casa_dos_dados[casa_dos_dados['empresa_buscada'] == empresa]['atividade_principal'].values[0]

    socios = eval(casa_dos_dados[casa_dos_dados['empresa_buscada'] == empresa]['quadro_societario'].values[0])

    st.write("**Aqui estão as informações sobre a empresa: **", empresa)

    st.write("**NOME: **", empresa)

    st.write("**CNPJ: **", cnpj)

    st.write("**RAZÃO SOCIAL: **", razao_social)

    st.write("**DATA DE ABERTURA: **", data_abertura)

    st.write("**SITUAÇÃO CADASTRAL: **", situacao_cadastral)

    st.write("**CAPITAL SOCIAL: **", capital_social)

    st.write("**NATUREZA JURIDICA: **", natureza_juridica)

    st.write("**LOCALIDADE: **", f'{municipio} / {uf}')

    st.write("**ATIVIDADE PRINCIPAL: **", atividade)

    st.selectbox("QUADRO SOCIETÁRIO: ", socios)

    st.header("QUEM DA MATCH COM ESTA EMPRESA?")
    st.text("Perfis que tem similalidades com as atividades da empresa")

    filtro = recomendacaot.filter(regex=(f"index|{empresa}")) # encontrar empresas recomendadas
    matches = filtro[filtro[empresa] == 'Recomendar']['index'].values # trazer a lista dos nomees recomendados


    matchesData = filtro[filtro[empresa] == 'Recomendar'][['index']] # DataFrame dos nomes recomendados

    dataCluster = matchesData.merge(perfis, left_on = 'index', right_on = 'nome') # Junção NomesRecomendados + Informações

    ExcelRec = dataCluster[dataCluster['cluster'] == 2].sort_values('soma_num', ascending = False)[:5] # Top 5 das Excelentes recomendações

    OtimRec = dataCluster[dataCluster['cluster'] == 0].sort_values('soma_num', ascending = False)[:5] # Top 5 das Ótimas recomendações

    BoaRec = dataCluster[dataCluster['cluster'] == 3].sort_values('soma_num', ascending = False)[:5] # Top 5 das Boas recomendações

    RuimRec = dataCluster[dataCluster['cluster'] == 1].sort_values('soma_num', ascending = False)[:5] # Top 5 das Ruins recomendações



    ERecomendado = st.radio("Conheça as 5 melhores recomendações: ", ExcelRec['nome'].values)
    # Para cada pessoa aqui clicada, mostrar as formações e experiencias

    st.write("Você selecionou: ", ERecomendado)

    ERecomendado_info = ExcelRec[ExcelRec['index'].str.contains(ERecomendado)]

    ERSobre = ERecomendado_info['sobre'].values[0]

    st.write("**Descricao: **", ERSobre)

    ERexp = eval(ERecomendado_info['experiencia'].values[0])


with c2:
    st.write("**SUAS EXPERIÊNCIAS ANTERIORES SÃO: **")
    for item in ERexp:
        st.write("**Cargo: **", item['cargo'])
        st.write("**Empresa: **", item['empresa'])
        st.write(" ")
    
with c3:
    ERformacao = eval(ERecomendado_info['formacao'].values[0])
    st.write("**SUAS FORMAÇÕES SÃO: **")
    for item in ERformacao:
        st.write("**Instituição: **", item['instituicao'])
        st.write("**Curso: **", item['curso'])
        st.write(" ")
    

with c4:
    ORecomendado = st.radio("Conheça as 5 outras opções de recomendação: ", OtimRec['nome'].values)
    # Para cada pessoa aqui clicada, mostrar as formações e experiencias

    st.write("Você selecionou: ", ORecomendado)

    ORecomendado_info = OtimRec[OtimRec['index'].str.contains(ORecomendado)]

    # ORSobre = ORecomendado_info['sobre'].values[0]

    # st.write("**Descricao: **", ORSobre)

    ORexp = eval(ORecomendado_info['experiencia'].values[0])

    st.write("**SUAS EXPERIÊNCIAS ANTERIORES SÃO: **")
    for item in ORexp:
        st.write("**Cargo: **", item['cargo'])
        st.write("**Empresa: **", item['empresa'])
        st.write(" ")
    
    ORformacao = eval(ORecomendado_info['formacao'].values[0])

    st.write("**SUAS FORMAÇÕES SÃO: **")
    for item in ORformacao:
        st.write("**Instituição: **", item['instituicao'])
        st.write("**Curso: **", item['curso'])
        st.write(" ")





    match_select = st.selectbox('Quer ver outras recomendações? ', matches)

    st.write("Você escolheu", match_select)



# with dataset:
#     st.header("QUEM DA MATCH COM ESTA EMPRESA?")
#     st.text("Perfis que tem similalidades com as atividades da empresa")





# with st.form(key='my_form'):
#     text_input = st.text_input(label='Enter your name')
#     submit_button = st.form_submit_button(label='Submit')


# with features:
#     st.header("Aqui vão as outras características")



