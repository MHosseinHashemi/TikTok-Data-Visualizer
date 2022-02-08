import numpy as np
import streamlit as st
import pandas as pd
from subprocess import call
import seaborn as sns
import plotly.express as px
from st_aggrid import AgGrid
import pickle

st.set_page_config(layout='wide')
st.sidebar.markdown("This dashboard allows you to analyse trending 📈 TikTok's.")

# Header
st.header('TikTok Data Analyzer')

def user_input_features():

    commentCount = st.sidebar.slider('commentCount', 0.0, 625700.0, 0.0)
    diggCount = st.sidebar.slider('diggCount', 22.0, 31000000.0, 22.0)
    shareCount = st.sidebar.slider('shareCount', 0.0, 220100.0, 0.0)
    videoMeta_duration = st.sidebar.slider('videoMeta_duration', 4.0, 60.0, 4.0)
    data = {
        'commentCount': commentCount,
        'diggCount': diggCount,
        'shareCount': shareCount,
        'videoMeta_duration': videoMeta_duration}
    features = pd.DataFrame(data, index=[0])
    return 
    
df = user_input_features()

st.subheader('User Inputs')
st.write(df)


# Load The Model
dt = pickle.load(open('reg.sav','rb'))

# Prediction
prediction = dt.predict(df)

st.subheader('Predicted Play Counts')
st.write(prediction)


# Input
hashtag = st.text_input('Search for a hashtag here', value="")

# Button
if st.button('Gather Data'):
    # Run get data function here
    call(['python', 'tiktok.py', hashtag])
    # Load in existing data to test it out
    df = pd.read_csv('tiktokdata.csv')
    
    # fig = sns.catplot(x="authorStats_heart", y="stats_playCount", hue="music_original" , kind="point", data=df)
    fig = sns.displot(df, x="stats_shareCount", kind="kde" , hue = 'author_verified', aspect=2,height=4,palette="Set2",fill=True)
    st.pyplot(fig)

    # fig = px.ecdf(df, x="music_duration", color="music_original")
    # fig_5 = sns.histplot(df, y="music_duration", x="video_duration", hue="music_original",palette="Set2")
    # st.pyplot(fig_5)

    # Split columns
    left_col, right_col = st.columns(2)

    # First Chart - video stats
    scatter1 = px.scatter(df, x='stats_shareCount', y='stats_commentCount', hover_data=['desc'], size='stats_playCount', color='stats_playCount')
    left_col.plotly_chart(scatter1, use_container_width=True)

    # Second Chart
    scatter2 = px.scatter(df, x='authorStats_videoCount', y='authorStats_heartCount', hover_data=['author_nickname'], size='authorStats_followerCount', color='authorStats_followerCount')
    right_col.plotly_chart(scatter2, use_container_width=True)


    # Show tabular dataframe in streamlit
    st.markdown('Tip: You can groupby or apply filter on the columns!')
    AgGrid(df)

    