import streamlit as st

st.set_page_config(
  page_title="kuliahpraktisi vitka",
  page_icon="🧊",
  layout="centered"
)


# Hirarki teks
st.title("viezzh")
st.header("when ya")
st.subheader("when ya")
st.caption("how r u?")
st.write("Hello, *backburner* :🫢:")

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)

if st.button("hey r u still there?"):
    st.write("good")
else:
    st.write("Goodbye")


st.button("Reset", type="primary")


col1, col2, col3 = st.columns(3)


st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")
