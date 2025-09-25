import streamlit as st
st.title("power calculator")
st.write("This app calculates the power of a number.")
n=st.number_input("Enter the base number (n):", value=2)
sq=n**2
cu=n**3
fith=n**5
st.write(f"The square of {n} is {sq}")
st.write(f"The cube of {n} is {cu}")
st.write(f"The fifth power of {n} is {fith}")