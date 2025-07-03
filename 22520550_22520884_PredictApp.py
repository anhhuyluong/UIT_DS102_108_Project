import streamlit as st
import pandas as pd
from predictor import predict_future_match, df_hist, model, team_mapping

st.title("⚽ Dự đoán kết quả trận đấu bóng đá của giải đấu Ngoại Hạng Anh")

# Select teams
home_team = st.selectbox("🔵 Chọn đội chủ nhà", list(team_mapping.keys()))
opponent = st.selectbox("🔴 Chọn đội khách", list(team_mapping.keys()))

# Input date
match_date = st.date_input("📅 Ngày trận đấu", pd.to_datetime("2022-01-01"))

# Dự đoán
if st.button("Dự đoán kết quả"):
    try:
        # Gọi hàm dự đoán
        prediction, probabilities = predict_future_match(
            home_team_name=home_team,
            opponent_name=opponent,
            date=match_date.strftime('%Y-%m-%d'),
            df_hist=df_hist,
            model=model,
            team_mapping=team_mapping
        )
        prediction_mapping = {
            'W': 'Thắng',
            'L': 'Thua',
            'D': 'Hòa'
        }
        result_text = prediction_mapping.get(prediction, prediction)
        proba_percent = dict(zip(["Thua", "Thắng", "Hòa"], [f"{p * 100:.1f}%" for p in probabilities]))


        st.success(f" Dự đoán: {home_team} sẽ **{result_text}** trước {opponent}")
        st.write("📊 Xác suất dự đoán:")
        #st.json(dict(zip(["L", "W", "D"], [round(p, 3) for p in probabilities])))
        st.json(proba_percent)
        st.warning("📌 Dự đoán chỉ mang tính chất tham khảo")
    except Exception as e:
        st.error(f"❌ Lỗi: {e}")