import streamlit as st

name = "rahul"

st.title("Find Letters in Word")

print_word = st.button("Show Word")

if print_word:
    st.write("rahul")
    st.write("Find letters in word")

num = st.number_input("Enter Number :", min_value=0, step=1)

if st.button("Submit"):

    if num == len(name):
        st.success("Congratulations")

    elif num < len(name):
        st.warning("Think Bigger Number")

    elif num > len(name):
        st.warning("Think Smaller Number")
