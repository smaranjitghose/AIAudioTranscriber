import streamlit as st
from streamlit_lottie import st_lottie 

import pathlib
import json
import re

def css_local(filepath:str):
    """
    Method to load the desired stylesheet from the given filepath
    """ 
    with open(filepath) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def lottie_local(filepath: str):
    """
    Method to load the desired Lottie Animation from the given filepath
    """
    with open(filepath, "r") as f:
        return json.load(f)


def lottie_url(url: str):
    """
    Method to load the desired Lottie Animation from given url
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def display_map(l1:list=[22.572645],l2:list=[88.363892],z:int=9)->None:
    """
    Method to display the desired coordinates in a map by using OpenStreetAPI

    Parameters
    -----------
    l1 : list
         desired latitude coordinate(s); default set for Kolkata ([22.572645])
    l2 : list
         desired longitude coordinate(s); default set for Kolkata ([88.363892])
    z  : int 
         desired zoom level; default set to metropolitan area level(9) 

    Returns
    --------
    None
    
    See Also
    --------
    For plotting multiple cities, simply pass their respective latitude and longitude coordinates in 
    the same list
    """
    map_data = pd.DataFrame({"latitude":np.array(l1),"longitude":np.array(l2)})
    st.map(map_data,zoom=z)

def hide_footer():
    hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

def validate_YT_link(url:str):
    """
    Function to check if the user provided YouTube URL is valid
    """
    pattern = r'https://www\.youtube\.com/watch\?v=[A-Za-z0-9]+'
    match = re.match(pattern, url)
    return match is not None



