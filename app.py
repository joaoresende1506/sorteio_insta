import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title='Sorteio Dra Mylena e Mare Acessórios')

# Título e subtítulo do aplicativo
st.title('Sorteio Dra. Mylena Braga e Mare Acessórios')
st.subheader('Boa sorte !')

# Divisor e informações sobre o sorteio
st.divider()
st.write('O sorteio irá funcionar da seguinte maneira:')
st.write(' - Todos os comentários realizados até o prazo definido pelo sorteio foram extraídos para uma planilha.')
st.write(' - Após o clique no botão será sorteado um número e iremos buscar dentro da planilha qual registro é esse comentário.')
st.caption('Obs: Os comentários foram ordenados de forma crescente pela data de registro.')
st.caption('Obs²: A hora está em formato e tempo civil americano.')

# Carrega os comentários da planilha
comentarios = pd.read_excel('comentarios.xlsx')

# Ordena os comentários pela hora
comentarios.sort_values(by='Hora', inplace=True)

# Variável de sessão para controlar a confirmação
if 'confirma' not in st.session_state:
    st.session_state.confirma = False


# Função para exibir o modal de confirmação
@st.experimental_dialog('Confirme sua ação')
def show_confirmation_modal():
    st.write("Tem certeza que deseja realizar o sorteio?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Sim', key='confirm_sorteio'):
            st.session_state.confirma = True
            st.rerun()
    with col2:
        if st.button('Não', key='cancel_sorteio'):
            st.session_state.confirma = False
            st.rerun()

# Botão para realizar o sorteio
if st.button('Sortear comentário'):
    show_confirmation_modal()

# Realiza o sorteio se confirmado
if st.session_state.confirma:
    st.balloons()
    # Seleciona um índice aleatório
    sorteado_idx = random.randint(0, len(comentarios) - 1)
    
    # Obtém o comentário sorteado
    comentario_sorteado = comentarios.iloc[sorteado_idx]
    
    # Exibe o comentário sorteado e o índice correspondente
    st.markdown(
        f'### Comentário sorteado: <span style="color:green; font-size: 2em;">{sorteado_idx}</span>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'### O(a) instagram do(a) sortudo(a) ganhador(a) do sorteio foi <span style="color:green; font-size: 2em;">{comentario_sorteado[0]}</span>',
        unsafe_allow_html=True
    )
    st.write(f'Com o comentário: {comentario_sorteado[1]}')
    st.write(f'Realizado no dia: {comentario_sorteado[2]}')
    st.session_state.confirma = False

if st.button('Limpar sorteio'):
    st.session_state.confirma = False
    st.experimental_rerun()

# Exibe todos os comentários
st.write('Esses são todos os comentários realizados:')
with st.expander('Comentários'):
    st.dataframe(comentarios)

# # Expander para os dados
# with st.expander('Dados'):
#     st.subheader('Análise das 15 pessoas que comentaram mais')

#     # Contagem de comentários por pessoa
#     comentarios_por_pessoa = comentarios['Nome'].value_counts()
#     total_comentarios = comentarios_por_pessoa.sum()

#     # Seleciona apenas os 10 maiores
#     top_15_comentarios = comentarios_por_pessoa.head(15)

#     # Porcentagem de chance de ganhar
#     chance_de_ganhar = (top_15_comentarios / total_comentarios) * 100

#     # Gráfico de rosca
#     fig, ax = plt.subplots()
#     ax.pie(top_15_comentarios, labels=top_15_comentarios.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))
#     ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#     st.pyplot(fig)

#     # Exibindo a tabela com a porcentagem de chance de ganhar
#     st.write('Porcentagem de chance de ganhar:')
#     st.dataframe(chance_de_ganhar.reset_index().rename(columns={'Nome': 'Nome', 'count': 'Chance (%)'}))
