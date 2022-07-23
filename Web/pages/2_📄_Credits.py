import streamlit as st
# from PIL import Image
# from pathlib import Path

st.set_page_config(
    page_title="Credits",
    page_icon="📄",
)

st.markdown(
    """
        ### Website Projek TA ini dibuat oleh:\n
        Ismatullah Hadi\n
        Renaldy Eka Putra\n


        ### Terima kasih untuk dosen pembimbing yang telah membimbing dan memberikan saran atas projek TA ini:\n
        Dr. Meta Kallista, S.Si., M.Si.\n
        Casi Setianingsih, S.T., M.T.\n\n
        .\n
        .\n
        Website ini dibuat menggunakan streamlit.
    """
)

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)