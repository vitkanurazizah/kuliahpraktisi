import streamlit as st

st.set_page_config(
  page_title="kuliahpraktisi vitka",
  page_icon="🧊",
  layout="centered"
)


# Hirarki teks
st.title("📊 Dashboard")
st.header("Laporan Bulanan")
st.subheader("📈 Monthly Expenses")
st.caption("Made with ❤️ using Streamlit")
st.write("Hello, *im mermaid!* :🧜🏻:")

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)
