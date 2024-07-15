import base64
import streamlit as st
import plotly.express as px
from utils import logo
from PIL import Image

report_page = st.Page("pages/fin_dash.py", title="Financial Dashboard", icon="📊")
watch_page = st.Page("pages/fin_watch.py", title="Watch List", icon="👁️")
tutor_page = st.Page("pages/fin_tutor.py", title="Financial Tutorial", icon="📖")

pg = st.navigation([report_page, watch_page, tutor_page])
st.set_page_config(page_title="Fin Fun", page_icon=":material/edit:")


def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url("https://raw.githubusercontent.com/andfanilo/social-media-tutorials/master/20221130-extras/logo.png");
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

add_logo()

img = get_img_as_base64("money_tree.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://pixabay.com/get/ge3a6d6033e6afed09113f8a57138139a4397c80648da98773484e8bd41657694af8e991e1dee43e5a30709f966b583f4103c2306625796116d54ed58bef94d2d_1280.png");
background-position: top left;
background-attachment: local;
}}
 
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)



pg.run()

