import streamlit as st
import datetime
from PIL import Image
img = Image.open("header house 2.PNG")
st.image(img, width=1000)
st.title('Welcome to Hunteazy')
st.subheader("Do you want to rent,buy or lease an apartment")
interest= st.selectbox("Please select your interest:", ['rent', 'buy','lease' ,'Others'])
if interest=="rent":
    interest=st.text('select apartment type')
if interest=='rent':
    interes=st.text('select apartment type')
elif interest=='lease':
    interest=st.text('select apartment type')
elif interest== 'Others':
     interest=st.text("wrong choice")
choice= st.selectbox("indicate apartment choice:", ['flat', 'duplex','land' ,'Others'])
if choice=="flat":
        choice=st.text('see available flats')


elif choice=="duplex":
        choice=st.text('see available duplexes')
        
elif choice== "land":
       choice=st.text('see available land')
elif choice=="Others":
        choice=st.text('wrong choice indicated') 
        

        
image = Image.open('insideflat.PNG')
st.image(image, caption='flat inside view')
image = Image.open('outside flat.PNG')
st.image(image, caption='flat outside view')

        
image = Image.open('outside duplex.PNG')

st.image(image, caption='Duplex outside view')

image = Image.open('inside duplex.PNG')
st.image(image, caption='Duplex inside view')


#viewing_date = st.date_input("Please select viewing date", min_value=datetime.date(1921, 1, 1),
# max_value=datetime.date(2030, 12, 31))
 

viewing_date = st.date_input(
     "Select your viewing date ",
     datetime.date(2019, 7, 6))
st.write('Your viewing date  is:', viewing_date)

st.text("Apartment choice and viewing date noted, An agent will contact you shortly")

