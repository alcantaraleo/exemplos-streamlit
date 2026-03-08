"""
Imagens e mídias no Streamlit

Este exemplo mostra como exibir imagem, áudio e vídeo na página.
Usamos uma URL pública para a imagem para o app funcionar sem arquivos extras.
Para áudio e vídeo, mostramos o código e uma mensagem explicativa.
"""

import streamlit as st

st.set_page_config(page_title="Imagens e mídias", layout="wide")
st.title("Imagens, áudio e vídeo")

# 3. Exibir resultado
# ----- IMAGEM -----
# st.image pode receber: arquivo local (caminho) ou URL da internet.
# caption = legenda que aparece embaixo da imagem.
st.header("Exibindo uma imagem")
url_imagem = (
    "https://streamlit.io/images/brand/streamlit-mark-color.png"
)
st.image(url_imagem, caption="Logo do Streamlit (fonte: documentação oficial)")

st.divider()

# ----- ÁUDIO -----
# st.audio recebe o caminho de um arquivo de áudio ou bytes.
# Formatos comuns: mp3, wav, ogg.
st.header("Áudio")
st.markdown(
    "Para exibir áudio, use **st.audio**. Exemplo com arquivo local: "
    "`st.audio('musica.mp3', format='audio/mp3')`. "
    "Coloque um arquivo .mp3 nesta pasta e descomente o código no app.py para testar."
)
# Exemplo (descomente e coloque um arquivo musica.mp3 na pasta):
# st.audio("musica.mp3", format="audio/mp3")

st.divider()

# ----- VÍDEO -----
# st.video recebe URL de vídeo (YouTube, etc.) ou caminho de arquivo.
st.header("Vídeo")
st.markdown(
    "Para exibir vídeo, use **st.video** com uma URL. "
    "Exemplo: um link do YouTube ou um arquivo .mp4 na pasta."
)
# Exemplo com URL (descomente para testar):
# st.video("https://www.youtube.com/watch?v=exemplo")

# Mensagem amigável para o público jovem
st.info(
    "Dica: você pode colocar suas próprias imagens, músicas e vídeos na pasta "
    "deste exemplo e mudar o código para usar o nome dos arquivos!"
)
