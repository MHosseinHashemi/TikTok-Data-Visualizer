import numpy as np
import streamlit as st
import pandas as pd
from subprocess import call
import plotly.express as px
from st_aggrid import AgGrid
import pickle
import plotly.graph_objects as go

st.set_page_config(layout='wide')
st.sidebar.markdown("<div><img src='https://png2png.com/wp-content/uploads/2021/08/Tiktok-logo-png.png' width=100 /><h1 style='display:inline-block'>Tiktok Analytics</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("This dashboard allows you to analyse trending 📈 TikTok's with Machine Learning algorithms.")

# Header
st.header('TikTok Data Analyzer')

# Just to show how it actualy looks like:
# st.sidebar.slider('commentCount', 0, 625700, 0)
# st.sidebar.slider('diggCount', 22, 31000000, 22)
# st.sidebar.slider('shareCount', 0, 220100)
# st.sidebar.slider('video_duration', 4, 60, 4)


def user_input_features():

    commentCount = st.sidebar.slider('commentCount', 0, 625700, 0)
    diggCount = st.sidebar.slider('diggCount', 22, 31000000, 22)
    shareCount = st.sidebar.slider('shareCount', 0, 220100, 1)
    video_duration = st.sidebar.slider('video_duration', 4, 60, 4)
    data = {
        'commentCount': commentCount,
        'diggCount': diggCount,
        'shareCount': shareCount,
        'video_duration': video_duration}
    features = pd.DataFrame(data, index=[0])
    return features
    
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
st.subheader('Now get live data from TikTok')
hashtag = st.text_input('Search for a hashtag here', value="")

# Button
if st.button('Gather Data'):
    # Run get data function here
    call(['python', 'tiktok.py', hashtag])
    # Load in existing data to test it out
    df = pd.read_csv('tiktokdata.csv')

    # read data and Create a scatter plot with a trendline
    data  = pd.read_csv('data_1.csv')
    
    fig = px.scatter(df, trendline="ols",
                    x="stats_shareCount", 
                    y="stats_commentCount",
                    labels={
                        "stats_shareCount": "Share Count",
                        "stats_commentCount": "Comments"
                    },
                    log_y=True,
                    trendline_color_override="#3351FF", 
                    template='plotly_white')

    fig.update_traces(marker=dict(
                        color='#FF3333',
                        opacity=0.7,
                    ))

    st.plotly_chart(fig, use_container_width=True)

    # Split columns
    left_col, right_col = st.columns(2)

    # First Chart - video stats
    scatter1 = px.scatter(df, x='stats_shareCount', y='stats_commentCount', hover_data=['desc'], size='stats_playCount', color='stats_playCount')
    left_col.plotly_chart(scatter1, use_container_width=True)

    # Second Chart
    scatter2 = px.scatter(df, x='authorStats_videoCount', y='authorStats_heartCount', hover_data=['author_nickname'], size='authorStats_followerCount', color='authorStats_followerCount')
    right_col.plotly_chart(scatter2, use_container_width=True)

    # Dataset EDA
    st.markdown('This is some Exploratory Data Analysis (EDA) on Gathered TikTok DataSet')

    fig_1 = px.histogram(data, x="musicMeta.musicAuthor", y="shareCount")
    st.plotly_chart(fig_1, use_container_width=True)

    # Read the file and start the Viz
    hashtags  = pd.read_csv('hashtags.csv')
    hashtags['count'] = 1
    hashtags = hashtags.groupby(["hashtag.name"])["count"].count().reset_index()
    hashtags = hashtags.sort_values(by='count', ascending=False)[:15]

    fig_2 = go.Figure(data=[go.Pie(
                            labels=hashtags["hashtag.name"], 
                            values=hashtags["count"], 
                            textinfo='label+percent',
                            insidetextorientation='radial'
                    )], 
                    layout={"colorway": ["#f72585","#b5179e",
                                        "#7209b7","#560bad",
                                        "#480ca8","#3a0ca3",
                                        "#3f37c9","#4361ee",
                                        "#4895ef","#4cc9f0"]})

    st.plotly_chart(fig_2, use_container_width=True) 

    # Grid the page
    left_col, right_col = st.columns(2)

    # Create a Pie Chart with all values
    fig_3 = px.scatter(data, x="diggCount", y="commentCount", animation_frame="videoMeta.duration", animation_group="hashtag.name",size='videoMeta.duration', color="authorMeta.verified", hover_name="shareCount") 
    # st.plotly_chart(fig_3, use_container_width=True)
    left_col.plotly_chart(fig_3, use_container_width=True)

    fig_4 = px.scatter(data, x="diggCount", y="shareCount", animation_frame="videoMeta.duration", animation_group="hashtag.name",size='videoMeta.duration', color="authorMeta.verified")
    right_col.plotly_chart(fig_4, use_container_width=True)

    # Show tabular dataframe in streamlit
    st.markdown('Tip: You can groupby or apply filter on the columns!')
    AgGrid(df)