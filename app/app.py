import os
import sys

# 1. Get the absolute path of the directory containing app.py (C:\Projects\AI Anime Recommender\app)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Get the parent directory (C:\Projects\AI Anime Recommender)
root_dir = os.path.dirname(current_dir)

# 3. Inject the root directory into Python's search path if it's not already there
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# ==========================================
# NOW you can safely import your project modules
# ==========================================
from pipeline.pipeline import AnimeRecommendationPipeline

# ... the rest of your streamlit app code goes here ...
import streamlit as st
#from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommnder",layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your anime prefernces eg. : light hearted anime with school settings")
if query:
    with st.spinner("Fetching recommendations for you....."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)

