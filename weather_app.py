import streamlit as st
import requests
from datetime import datetime

# --- Page Config ---
st.set_page_config(page_title="Global Weather Radar", page_icon="🌤️")

# --- Title Area ---
st.title("🌍 Global Real-Time Weather Radar")
st.caption("Powered by OpenWeatherMap API | Developed by Yang-Tech-Lab")

# --- Sidebar ---
st.sidebar.header("⚙️ Control Panel")
city = st.sidebar.text_input("Enter City Name (e.g., London):", "New York")
check_btn = st.sidebar.button("🚀 Search Now")

# --- Core Logic ---
api_key = "103104f0c64435943e54807674a02704" # 你的 Key
# 注意：这里去掉了 lang=zh_cn，这样 API 也会返回英文的天气描述 (e.g. Clear Sky)
base_url = "http://api.openweathermap.org/data/2.5/weather"

if check_btn:
    with st.spinner('Connecting to satellite...'):
        try:
            # Request Data
            url = f"{base_url}?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                
                # Extract Data
                temp = data['main']['temp']
                feels_like = data['main']['feels_like']
                desc = data['weather'][0]['description'].title() # 首字母大写
                humidity = data['main']['humidity']
                wind = data['wind']['speed']
                icon_code = data['weather'][0]['icon']
                
                # --- Display Data ---
                
                # 1. Weather Icon (Fixed HTTPS issue)
                icon_url = f"https://openweathermap.org/img/wn/{icon_code}@4x.png"
                st.image(icon_url, width=100)
                
                # 2. Key Metrics
                col1, col2, col3 = st.columns(3)
                col1.metric("Temperature", f"{temp}°C", f"Feels like {feels_like}°C")
                col2.metric("Humidity", f"{humidity}%")
                col3.metric("Wind Speed", f"{wind} m/s")
                
                # 3. Status Message
                st.success(f"Current weather in **{city}**: **{desc}**")
                
                # 4. Raw Data (For Geeks)
                with st.expander("View Raw JSON Data"):
                    st.json(data)
                    
            else:
                st.error("❌ City not found! Please check the spelling.")
                
        except Exception as e:
            st.error(f"Connection Error: {e}")

else:
    st.info("👈 Please enter a city name in the sidebar to start.")