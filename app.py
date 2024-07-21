import requests
import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Quick Recipe",
    page_icon="icon.png",
    menu_items={
        "About":"Quick Recipe is your hassle-free tool for discovering recipes. Quickly find meals that match your taste and dietary needs with our easy-to-use search. Enjoy cooking with Quick Recipe!"
    }
)

st.write("<h2 style=color:#FF6F00;>Instant Meals for Instant Gratification.</h2>",unsafe_allow_html=True)

query=st.text_input("Add Your Recipe Here",placeholder="matar paneer")
language=st.radio("Select your language",["English","Hindi"])
btn=st.button("Search Recipes")

def display_data(i):

    st.write(f"<h3 style='color:#98FF98;font-size:30px;'>{GoogleTranslator(target=language).translate(i['title'])}</h3>", unsafe_allow_html=True)

    if len(i["ingredients"]) != 0:
        st.write(f"<h3>{GoogleTranslator(target=language).translate('Ingredients -')}</h3>", unsafe_allow_html=True)
        for j in GoogleTranslator(target=language).translate(i["ingredients"]).split("|"):
            st.write(f"<li style='font-size:18px;'>{j}</li>", unsafe_allow_html=True)

    st.write(f"<h3>{GoogleTranslator(target=language).translate('Instructions -')}</h3>", unsafe_allow_html=True)

    st.write(f"<p style='font-size:18px;'>{GoogleTranslator(target=language).translate(i['instructions'])}</p>", unsafe_allow_html=True)

    st.write(f"<h4>→ {GoogleTranslator(target=language).translate('This recipe yields ' + str(i['servings'])+".")}</h4>", unsafe_allow_html=True)

if btn:
    if language=="English":
        language="en"
    else:
        language="hi"
    try:
        api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)
        response = requests.get(api_url, headers={'X-Api-Key': '2jWCY0dASiPZc7RLybXvXA==R9oC0XPKPWiGJ6k6'})
        if response.status_code == requests.codes.ok:
            data=response.json()
            if(len(data)>=1):
                for i in data:
                    display_data(i)
            else:
                st.info("Recipe Not Found")
    except:
        st.error("Network Error")
