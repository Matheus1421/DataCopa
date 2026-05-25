import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go

st.set_page_config(
    page_title="Raio-X da Seleção",
    page_icon="🇧🇷",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .titulo-brasil {
        background: -webkit-linear-gradient(45deg, #009C3B, #FFDF00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 0px;
    }
    .subtitulo {
        text-align: center; color: #A0AEC0; font-size: 1.2rem; margin-bottom: 40px;
    }
    hr { border-color: #002776 !important; border-width: 2px !important; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def carregar_dados():
    caminho_base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'processed'))
    df_equipe = pd.read_csv(f"{caminho_base}/desempenho_equipe.csv")
    df_artilheiros = pd.read_csv(f"{caminho_base}/dependencia_artilheiros.csv")
    df_cartoes = pd.read_csv(f"{caminho_base}/disciplina_cartoes.csv")
    return df_equipe, df_artilheiros, df_cartoes

try:
    df_equipe, df_artilheiros, df_cartoes = carregar_dados()
    st.session_state['dados_ok'] = True
except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    st.session_state['dados_ok'] = False

#Header, Subtítulo e KPI's
st.markdown('<p class="titulo-brasil">🏆 Raio-X Histórico: Seleção Brasileira</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">A evolução de desempenho, artilharia e disciplina tática em todas as Copas do Mundo</p>', unsafe_allow_html=True)

#Corpo da interação
if st.session_state.get('dados_ok'):
    
    total_gols = int(df_equipe['Gols Feitos'].sum())
    total_copas = df_equipe['Year'].nunique()
    saldo_total = int(df_equipe['Saldo de Gols'].sum())
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric(label="Títulos Mundiais", value="5", delta="Único Pentacampeão", delta_color="normal")
    with col2: st.metric(label="Participações em Copas", value=f"{total_copas}", delta="Todas as edições", delta_color="off")
    with col3: st.metric(label="Gols Marcados", value=f"{total_gols}", delta="Maior ataque da história", delta_color="normal")
    with col4: st.metric(label="Saldo Histórico", value=f"+{saldo_total}", delta="Gols Pró - Contra", delta_color="off")

    st.markdown("---")

    aba1, aba2, aba3 = st.tabs(["⚽ Desempenho e Gols", "🎯 Artilharia e Dependência", "🟨🟥 Disciplina Tática"])
    
    # --- ABA 1: DESEMPENHO DA EQUIPE ---
    with aba1:
        st.markdown("### A Máquina de Fazer Gols")
        
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(x=df_equipe['Year'], y=df_equipe['Gols Feitos'], name='Gols Pró', marker_color='#009C3B'))
        fig1.add_trace(go.Bar(x=df_equipe['Year'], y=df_equipe['Gols Sofridos'], name='Gols Sofridos', marker_color='#D90429'))
        fig1.add_trace(go.Scatter(x=df_equipe['Year'], y=df_equipe['Saldo de Gols'], name='Saldo', mode='lines+markers', line=dict(color='#FFDF00', width=3)))
        
        fig1.update_layout(
            template='plotly_dark', barmode='group',
            xaxis=dict(title='Ano da Copa', tickmode='array', tickvals=df_equipe['Year'], tickangle=-45),
            yaxis=dict(title='Quantidade de Gols', gridcolor='#333333'),
            hovermode='x unified', margin=dict(l=40, r=40, t=40, b=40),
            plot_bgcolor='#0E1117', paper_bgcolor='#0E1117',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
        )
        st.plotly_chart(fig1, use_container_width=True)
        
    # --- ABA 2: ARTILHARIA E DEPENDÊNCIA ---
    with aba2:
        st.markdown("### Quem Chamou a Responsabilidade?")
        
        tabela_estilizada = (
            df_artilheiros.style
            .format({
                'Dependência (%)': '{:.1f}%', 
                'Year': '{}',
                'Gols do Time': '{}',        
                'Gols do Artilheiro': '{}'   
            })
            .background_gradient(subset=['Dependência (%)'], cmap='OrRd')
        )
        
        st.dataframe(tabela_estilizada, use_container_width=True, hide_index=True)
        
    # --- ABA 3: DISCIPLINA TÁTICA ---
    with aba3:
        st.markdown("### O Peso da Camisa")
        
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(
            x=df_cartoes['Year'], y=df_cartoes['Cartões Amarelos'], name='Amarelos',
            mode='lines+markers', line=dict(color='#FFC300', width=3),
            marker=dict(size=8, line=dict(color='white', width=1)),
            stackgroup='one', fillcolor='rgba(255, 195, 0, 0.4)'
        ))
        fig3.add_trace(go.Scatter(
            x=df_cartoes['Year'], y=df_cartoes['Cartões Vermelhos'], name='Vermelhos',
            mode='lines+markers', line=dict(color='#D90429', width=3),
            marker=dict(size=8, line=dict(color='white', width=1)),
            stackgroup='one', fillcolor='rgba(217, 4, 41, 0.6)'
        ))
        
        fig3.update_layout(
            template='plotly_dark',
            xaxis=dict(title='Ano da Copa', tickmode='array', tickvals=df_cartoes['Year'], tickangle=-45, showgrid=False),
            yaxis=dict(title='Volume de Cartões', gridcolor='#333333', zeroline=True, zerolinecolor='#555555'),
            hovermode='x unified', margin=dict(l=40, r=40, t=40, b=40),
            plot_bgcolor='#0E1117', paper_bgcolor='#0E1117',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
        )
        
        fig3.add_shape(type="line", x0=1939, y0=2, x1=1949, y1=2, line=dict(color="#666666", width=2, dash="solid"))
        fig3.add_shape(type="line", x0=1939, y0=1.5, x1=1939, y1=2.5, line=dict(color="#666666", width=2))
        fig3.add_shape(type="line", x0=1949, y0=1.5, x1=1949, y1=2.5, line=dict(color="#666666", width=2))
        fig3.add_annotation(x=1944, y=3, text="2ª Guerra", showarrow=False, font=dict(color="#AAAAAA", size=10))
        fig3.add_annotation(x=1970, y=18, text="Início dos<br>Cartões", showarrow=True, arrowhead=1, ax=-40, ay=-30, font=dict(color="#AAAAAA", size=10))
        
        st.plotly_chart(fig3, use_container_width=True)

else:
    st.warning("Verifique o caminho dos seus arquivos CSV na pasta 'processed'.")