import streamlit as st

name = "rahul"

st.title("Find Letters Game")

st.write("Guess how many letters are in the word.")

num = st.number_input(
    "Enter Number",
    min_value=1,
    step=1
)

if st.button("Check"):

    if num == len(name):
        st.success("🎉 Congratulations!")

    elif num < len(name):
        st.warning("Think Bigger Number")

    else:
        st.warning("Think Smaller Number")
