import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title = "My Webpage", page_icon =":tada", layout = "wide")

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")


#loading assets
lottie_coding = load_lottieurl("https://lottie.host/9e40ab02-9bff-4474-ac00-77859c1cbafa/NKKlXTjyhs.json")
img_contact_form =Image.open("images/download1.png")
img_lottie_animation = Image.open("images/download2.png")


# Header section
with st.container():
    st.subheader("Hi, I am Godwin :wave")
    st.title("I am a Business Analyst fro Johannesburg")
    st.write("I am passionate about all things technology related")
    st.write("[My main website >](http://godwinahmed.co.za)")


# what i do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header(""" 
                  What I do
                  -
                  -
                  """)
        st.write("##")
        st.write(" All about me")
        #Links to sites 
        st.write("[LinkedIn>](#########)")
        st.write("[Youtube>](#########)")
        st.write("[Twitter>](#########)")

# right column 
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

# Projects 
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        #insert image
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Portfolio of projects")
        st.write("""
                Insert your portfolio of projects 
                """)
        st.markdown("[Watch video ...](https://youtube.com)")
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        #insert image
        st.image(img_contact_form)
    with text_column:
        st.subheader("Portfolio of projects")
        st.write("""
                Insert your portfolio of projects 
                """)
        st.markdown("[Watch video ...](https://youtube.com)")
# Contact form
with st.container():
    st.write("---")
    st.header("Get in touch, lets talk about tech..")
    st.write("##")
    # create contact form
    contact_form = """ 
    <form action="https://formsubmit.co/godwina.ga@gmail.com" method="POST">
        <input type = "hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder = "Your Name" required>
        <input type="email" name="email" placeholder = "Your Email addres" required>
        <textarea name ="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
