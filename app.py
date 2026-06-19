import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="WhatsApp Analyzer Pro",
    page_icon="💬",
    layout="wide"
)

st.title("💬 WhatsApp Chat Analyzer Pro")

st.markdown("""
<style>
.big-font {font-size:22px !important; font-weight:600;}
.card {
    padding: 15px;
    border-radius: 10px;
    background-color: #f5f5f5;
}
</style>
""", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.sidebar.file_uploader("Upload Chat File")

if uploaded_file:

    with st.spinner("Processing chat..."):
        time.sleep(1)

        data = uploaded_file.getvalue().decode("utf-8")
        df = preprocessor.preprocess(data)

    user_list = df['user'].unique().tolist()
    user_list = [u for u in user_list if u != 'group_notification']
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Select User", user_list)

    if st.sidebar.button("Analyze 🚀"):

        st.success("Analysis Complete!")

        # ---------------- STATS ----------------
        msg, words, media, links = helper.fetch_stats(selected_user, df)

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Messages", msg)
        col2.metric("Words", words)
        col3.metric("Media", media)
        col4.metric("Links", links)

        st.divider()

        # ---------------- TABS ----------------
        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Trends",
            "👥 Users",
            "☁️ WordCloud",
            "😀 Emojis"
        ])

        # -------- TAB 1 --------
        with tab1:

            st.subheader("Activity Trends")

            timeline = helper.monthly_timeline(selected_user, df)

            fig, ax = plt.subplots()
            ax.plot(timeline['time'], timeline['message'], marker='o')
            plt.xticks(rotation=45)
            st.pyplot(fig)

            daily = helper.daily_timeline(selected_user, df)

            fig, ax = plt.subplots()
            ax.plot(daily['only_date'], daily['message'], color='green')
            st.pyplot(fig)

                    # ================= HEATMAP =================
            st.subheader("🔥 Weekly Activity Heatmap")

            heatmap = helper.activity_heatmap(selected_user, df)

            fig, ax = plt.subplots(figsize=(12, 5))
            sns.heatmap(heatmap, ax=ax, cmap="YlGnBu")
            st.pyplot(fig)

        # -------- TAB 2 --------
        with tab2:

            if selected_user == "Overall":

                st.subheader("Top Active Users")

                x, new_df = helper.most_busy_users(df)

                col1, col2 = st.columns(2)

                with col1:
                    fig, ax = plt.subplots()
                    ax.bar(x.index, x.values, color="red")
                    st.pyplot(fig)

                with col2:
                    st.dataframe(new_df)

            else:
                st.info("Select 'Overall' for user comparison")

        # -------- TAB 3 --------
        with tab3:

            st.subheader("Word Cloud")

            wc = helper.create_wordcloud(selected_user, df)

            fig, ax = plt.subplots()
            ax.imshow(wc)
            ax.axis("off")
            st.pyplot(fig)

        # -------- TAB 4 --------
        with tab4:

            st.subheader("Emoji Analysis")

            emoji_df = helper.emoji_helper(selected_user, df)

            if not emoji_df.empty:

                col1, col2 = st.columns(2)

                with col1:
                    st.dataframe(emoji_df)

                with col2:
                    fig, ax = plt.subplots()
                    ax.pie(
                        emoji_df['count'].head(10),
                        labels=emoji_df['emoji'].head(10),
                        autopct="%1.1f%%"
                    )
                    st.pyplot(fig)

            else:
                st.warning("No emojis found")
else:
    st.info("Upload a WhatsApp chat file to start analysis")