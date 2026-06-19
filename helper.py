from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji
import numpy as np

extract = URLExtract()

# ---------------- STATS ----------------
def fetch_stats(user, df):

    if user != "Overall":
        df = df[df['user'] == user]

    messages = df.shape[0]
    words = df['message'].str.split().str.len().sum()
    media = df['message'].str.contains('<Media omitted>').sum()

    links = df['message'].apply(lambda x: len(extract.find_urls(str(x)))).sum()

    return messages, words, media, links


# ---------------- BUSY USERS ----------------
def most_busy_users(df):

    x = df['user'].value_counts().head(10)

    percent_df = round((df['user'].value_counts() / len(df)) * 100, 2)\
        .reset_index()

    percent_df.columns = ['user', 'percent']

    return x, percent_df


# ---------------- WORDCLOUD ----------------
def create_wordcloud(user, df):

    if user != "Overall":
        df = df[df['user'] == user]

    df = df[df['message'] != "<Media omitted>"]

    wc = WordCloud(
        width=800,
        height=400,
        background_color="white"
    )

    text = " ".join(df['message'].astype(str).tolist())

    return wc.generate(text)


# ---------------- COMMON WORDS ----------------
def most_common_words(user, df):

    if user != "Overall":
        df = df[df['user'] == user]

    words = []

    for msg in df['message']:
        words.extend(str(msg).lower().split())

    return pd.DataFrame(Counter(words).most_common(20))


# ---------------- EMOJIS (FIXED + CLEAN) ----------------
def emoji_helper(user, df):

    if user != "Overall":
        df = df[df['user'] == user]

    emojis = []

    for msg in df['message']:
        emojis.extend([c for c in str(msg) if c in emoji.EMOJI_DATA])

    return pd.DataFrame(Counter(emojis).most_common(), columns=['emoji', 'count'])


# ---------------- TIMELINES ----------------
def monthly_timeline(user, df):

    if user != "Overall":
        df = df[df['user'] == user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    timeline['time'] = timeline['month'] + "-" + timeline['year'].astype(str)

    return timeline


def daily_timeline(user, df):

    if user != "Overall":
        df = df[df['user'] == user]

    return df.groupby('only_date').count()['message'].reset_index()


# ---------------- ACTIVITY MAP ----------------
def week_activity_map(user, df):

    if user != "Overall":
        df = df[df['user'] == user]

    return df['day_name'].value_counts()


def month_activity_map(user, df):

    if user != "Overall":
        df = df[df['user'] == user]

    return df['month'].value_counts()


def activity_heatmap(user, df):

    if user != "Overall":
        df = df[df['user'] == user]

    return df.pivot_table(
        index='day_name',
        columns='period',
        values='message',
        aggfunc='count'
    ).fillna(0)