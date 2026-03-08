"""
Página "Sobre o Problema" - Ligação com o ODS 12

Aqui explicamos de forma didática:
- O que é o ODS 12
- Por que o desperdício de alimentos é um problema
- Como este app se conecta ao objetivo

Linguagem simples para crianças e adolescentes (8 a 18 anos).
"""

import streamlit as st

# ----- Título -----
st.title("📖 Sobre o Problema")
st.markdown("### Entenda a ligação com o ODS 12 da ONU")

st.divider()

# ----- O que é ODS 12 -----
st.subheader("🌍 O que é o ODS 12?")
st.markdown(
    "Os **Objetivos de Desenvolvimento Sustentável** (ODS) são metas que os países "
    "do mundo todo combinaram de alcançar até 2030. São 17 objetivos para tornar "
    "o planeta mais justo, saudável e sustentável."
)
st.markdown(
    "O **ODS 12** trata de **Consumo e Produção Responsáveis**. Isso significa: "
    "usar os recursos do planeta de forma inteligente, sem desperdiçar."
)

st.info(
    "💡 **Em resumo:** O ODS 12 quer que a gente consuma de forma consciente "
    "e reduza o desperdício – inclusive de comida!"
)

st.divider()

# ----- Por que o desperdício de alimentos é um problema -----
st.subheader("🍎 Por que o desperdício de alimentos é um problema?")

col_esq, col_dir = st.columns(2)

with col_esq:
    st.markdown(
        "**1. Muita gente passa fome**  \n"  \n"
        "Enquanto jogamos comida fora, milhões de pessoas no mundo não têm o que comer.\n\n"
        "**2. Desperdiça recursos**  \n"
        "Para produzir comida, usamos água, terra, energia. Desperdiçar comida = desperdiçar tudo isso.\n\n"
        "**3. Polui o meio ambiente**  \n"
        "Comida no lixo pode gerar gases que aquecem o planeta."
    )

with col_dir:
    st.markdown(
        "**4. Custa dinheiro**  \n"
        "Comprar e jogar fora é dinheiro perdido.\n\n"
        "**5. É um hábito que podemos mudar**  \n"
        "Registrar o que desperdiçamos nos ajuda a perceber e diminuir."
    )

st.divider()

# ----- Como este app ajuda -----
st.subheader("🛠️ Como este app ajuda?")

st.markdown(
    "Este app foi criado como **exemplo** para o Technovation (programa que ensina "
    "meninas a criar soluções com tecnologia). Ele serve para:"
)

st.markdown(
    "- **Registrar** o que você desperdiçou (nome do alimento + quantidade)\n"
    "- **Acompanhar** ao longo do tempo (gráfico de evolução)\n"
    "- **Refletir** sobre seus hábitos e tentar reduzir o desperdício\n\n"
    "**Ideia:** Quando a gente mede algo, fica mais fácil melhorar!"
)

st.success(
    "👉 Use o **Dashboard** para começar a registrar. "
    "Com o tempo, você pode ver se está desperdiçando menos!"
)

st.divider()
st.caption(
    "Fonte: Objetivos de Desenvolvimento Sustentável - ONU Brasil • "
    "Projeto exemplo Technovation"
)
