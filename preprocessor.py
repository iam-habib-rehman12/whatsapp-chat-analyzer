import re
import pandas as pd

def preprocess(data):

    # -------- Robust WhatsApp pattern --------
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s(?:am|pm|AM|PM)'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({"user_message": messages, "date": dates})

    # -------- Safe datetime parsing --------
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    df.dropna(subset=['date'], inplace=True)

    # -------- Split user & message (robust) --------
    users = []
    msgs = []

    for msg in df['user_message']:

        entry = re.split(r'([^:]+):\s', msg, maxsplit=1)

        if len(entry) > 2:
            users.append(entry[1].strip())
            msgs.append(entry[2].strip())
        else:
            users.append("group_notification")
            msgs.append(entry[0].strip())

    df['user'] = users
    df['message'] = msgs
    df.drop(columns=['user_message'], inplace=True)

    # -------- Feature engineering --------
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['month_num'] = df['date'].dt.month
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour

    # -------- Smart time periods --------
    df['period'] = df['hour'].apply(
        lambda h: f"{h:02d}-{(h+1)%24:02d}"
    )

    return df