import streamlit as st

#Streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square , cube  and fifth power")

# Get User input
n= st.number_input("ENter an inetger, value=1,step=1")

#Calculate results
square =  n ** 2
cube = n ** 3
fifith_power = n ** 5

#Display results
st.write(f"The square of {n} is : {square}")
st.write(f"The cube of {n} is : {cube}")
st.write(f"The fifth power of {n} is: {fifith_power}")