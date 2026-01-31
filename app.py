import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURATION DE LA PAGE (Look Mobile & App) ---
st.set_page_config(
    page_title="Architecte de Prompt Pro",
    page_icon="🎨",
    layout="centered", # Centré pour un meilleur rendu sur téléphone
    initial_sidebar_state="collapsed"
)

# --- 2. TA TOUCHE PERSONNELLE (LES RECETTES) ---
# Ces signatures seront injectées dans l'IA pour créer ton style unique
MY_SIGNATURES = {
    "💎 Luxe": "High-end product photography, matte textures, soft studio lighting, neutral tones, elegant.",
    "🔥 Brut": "Anamorphic lens, high contrast, gritty textures, 35mm film grain, moody atmosphere.",
    "🌈 Pastel": "Ethereal glow, soft focus, pastel colors, whimsical lighting, Studio Ghibli style.",
    "⚡ Cyber": "Neon bioluminescence, futuristic materials, electric blue accents, ultra-detailed.",
    "🌿 Nature": "National Geographic style, macro photography, natural volumetric lighting, hyper-realistic.",
    "🎨 Sketch": "Blueprint aesthetic, fine ink lines, watercolor washes, architectural masterpiece."
}

# --- 3. CONFIGURATION API ---
# Remplace par ta clé API gratuite de Google AI Studio
# (https://aistudio.google.com/)

