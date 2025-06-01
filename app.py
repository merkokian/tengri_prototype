import streamlit as st
import json
from rituals.sky_ritual import perform_ritual

st.set_page_config(page_title="Tengri.exe Ritüel Simülatörü")
st.title("🌌 Tengri.exe Ritüel Başlatıcı")

if st.button("🔮 Ritüeli Başlat"):
    result = perform_ritual()

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
