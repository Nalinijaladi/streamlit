
import streamlit as st
st.title("Hello")

st.header("Deploying using :blue[Streamlit Cloud]")

agree = st.checkbox("I agree with lal.")

if agree:
    st.write("You are great!")



genre = st.radio(
    "What's your favorite movie genre",
    ["[Comedy]", "Drama", "Documentary"]
)

if genre == "[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

number1 = st.number_input("Insert a number")
number2 = st.number_input("Insert another number")



if st.button("add"):
    st.write("sum of numbers is : ", number1 + number2)


