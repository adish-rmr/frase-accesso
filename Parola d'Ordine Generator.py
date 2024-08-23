import streamlit as st
import random

random.seed()
lista = []
password = []
parole = 4

with open("paroleitaliane/60000_parole_italiane.txt") as file:
    for line in file:
        lista.append(line)

st.image("logo2.png")
st.subheader("Generatore di frasi d'accesso casuali in italiano", divider="grey")

col1, col2 = st.columns([1,7])

with col1:
    st.write("  ")
    if st.button("Genera", type="primary"):
        for t in range(parole):
            password.append(random.choice(lista))
            password[t] = password[t][:-1]

with col2:
    parole = st.slider("Da quante parole vuoi che sia composta la frase?", 1, 8, 4)

st.code("-".join(password))


