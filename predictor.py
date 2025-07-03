import pandas as pd
import joblib
import numpy as np

df_hist = pd.read_csv('gold_FPro_data_combination.csv')

model = joblib.load('Final_chosen_model.pkl')

team_mapping = {
    'Tottenham': 0,
    'Chelsea': 1,
    'Manchester Utd': 2,
    'Liverpool': 3,
    'Everton': 4,
    'Arsenal': 5,
    'Manchester City': 6,
    'Brighton': 7,
    'Newcastle Utd': 8,
    'West Ham': 9,
    'Crystal Palace': 10
}

def predict_future_match(home_team_name, opponent_name, date, df_hist, model, team_mapping, window=3):
    """
    Hàm predict_future_match sẽ nhận các tham số đầu vào gồm:
    - Tên các đội chủ nhà, đội khách
    - Ngày diễn ra trận đấu
    - Dữ liệu lịch sử
    - Mô hình dự đoán
    - Danh sách ánh xạ tên các đội bóng sang giá trị số
    Hàm này thực hiện việc dự đoán kết quả trận đấu dựa trên trung bình 3 trận đấu trước đó
    """
    home_code = team_mapping.get(home_team_name)
    opp_code = team_mapping.get(opponent_name)
    if home_code is None or opp_code is None:
        raise ValueError("Tên đội không nằm trong danh sách team_mapping.")
    elif home_code == opp_code:
        raise ValueError("Hai đội không thể cùng tên")

    df = df_hist.copy()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[df['Date'] < pd.to_datetime(date)]

    recent_home = df[df['hometeam_code'] == home_code].sort_values(by='Date').tail(window)

    h2h = df[(df['hometeam_code'] == home_code) & (df['opponent_code'] == opp_code)].sort_values(by='Date').tail(window)

    features = df.drop(columns=['Date', 'target']).columns.tolist()

    input_dict = {}

    for feat in features:
        if feat == 'hometeam_code':
            input_dict[feat] = home_code
        elif feat == 'opponent_code':
            input_dict[feat] = opp_code
        elif feat.startswith('h2h_avg_'):
            input_dict[feat] = h2h[feat].mean() if feat in h2h.columns and not h2h.empty else 0.0
        elif feat.endswith('_rolling'):
            input_dict[feat] = recent_home[feat].mean() if feat in recent_home.columns and not recent_home.empty else 0.0
        elif feat == 'venue_code':
            input_dict[feat] = 1
        else:
            input_dict[feat] = recent_home[feat].mean() if feat in recent_home.columns and not recent_home.empty else 0.0

    X_input = pd.DataFrame([input_dict])
    prediction = model.predict(X_input)[0]
    probas = model.predict_proba(X_input)[0]
    label_map = {0: 'L', 1: 'W', 2: 'D'}

    return label_map[prediction], probas
