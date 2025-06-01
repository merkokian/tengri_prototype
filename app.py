import os
import streamlit as st
import json
from rituals.sky_ritual import perform_ritual
from datetime import datetime
from ai.analyzer import analyze_ritual

st.set_page_config(page_title="Tengri.exe Ritüel Simülatörü")
st.title("🌌 Tengri.exe Ritüel Başlatıcı")

if st.button("🔮 Ritüeli Başlat"):
    result = perform_ritual()

    # LOG klasörü oluşturuluyor
    os.makedirs("outputs/logs", exist_ok=True)

    # Zaman damgası ile log dosyası
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = f"outputs/logs/result_{timestamp}.json"

    # Log dosyasına yaz
    with open(log_path, "w") as f:
        json.dump(result, f, indent=2)

    # Son sonucu da güncelle
    with open("outputs/results.json", "w") as f:
        json.dump(result, f, indent=2)

    st.success("Ritüel tamamlandı!")
    st.json(result)

if st.button("📄 Sonuçları Göster"):
    try:
        with open("outputs/results.json") as f:
            data = json.load(f)
        st.json(data)
    except FileNotFoundError:
        st.warning("Henüz ritüel sonucu yok. Önce başlat!")

if st.button("🧠 Yorumla"):
    try:
        with open("outputs/results.json") as f:
            ritual_data = json.load(f)

        st.info("Ritüel verisi GPT'ye gönderiliyor...")
        analysis = analyze_ritual(ritual_data)
        st.markdown("### 🔍 GPT Yorumlama")
        st.write(analysis)

    except FileNotFoundError:
        st.warning("Henüz analiz edilecek bir ritüel sonucu yok.")
