import streamlit as st

st.title("💪 Beden Kitle İndeksi Hesaplama")

boy = st.number_input("Boyunuzu metre cinsinden giriniz (örn: 1.70)", min_value=0.5, max_value=2.5, step=0.01)
kilo = st.number_input("Kilonuzu giriniz (kg)", min_value=1, max_value=300, step=1)

if st.button("Hesapla"):
    kitle_indeksi = kilo / (boy ** 2)
    st.success(f"Beden Kitle İndeksiniz: {kitle_indeksi:.2f}")

    if kitle_indeksi < 18.5:
        st.warning("Zayıf")
    elif 18.5 <= kitle_indeksi < 24.9:
        st.info("Normal kiloda")
    elif 25 <= kitle_indeksi < 29.9:
        st.warning("Fazla kilolu")
    else:
        st.error("Obez")
