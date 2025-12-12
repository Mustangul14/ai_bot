import streamlit as st
import ollama
import time
from datetime import datetime

# Configurare pagină
st.set_page_config(
    page_title="Asistent AI Personal",
    page_icon="🤖",
    layout="wide"
)

# CSS personalizat
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
    }
    .chat-header {
        text-align: center;
        color: white;
        padding: 20px;
        font-size: 2.5em;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
</style>
""", unsafe_allow_html=True)

# Header personalizat
st.markdown('<div class="chat-header">🤖 Asistentul Tău AI Personal</div>', unsafe_allow_html=True)

# Sidebar cu setări
with st.sidebar:
    st.header("⚙️ Setări")
    
    # Selectare model
    available_models = ["phi3", "llama2", "mistral", "gemma"]
    selected_model = st.selectbox(
        "Alege modelul AI:",
        available_models,
        index=0
    )
    
    # Personalizare prompturi sistem
    st.subheader("🎭 Personalitate AI")
    personality = st.radio(
        "Alege stilul de conversație:",
        ["Prietenos", "Profesional", "Creativ", "Tehnic", "Personalizat"]
    )
    
    # Prompturi predefinite
    personality_prompts = {
        "Prietenos": "Ești un asistent AI prietenos, călduroș și empatic. Răspunzi într-un mod conversațional și accesibil.",
        "Profesional": "Ești un asistent AI profesional și eficient. Oferi răspunsuri clare, concise și bine structurate.",
        "Creativ": "Ești un asistent AI creativ și imaginativ. Folosești metafore, exemple interesante și abordări inovatoare.",
        "Tehnic": "Ești un expert tehnic care oferă răspunsuri detaliate, precise și cu exemple de cod când este relevant.",
        "Personalizat": ""
    }
    
    if personality == "Personalizat":
        custom_prompt = st.text_area(
            "Descrie personalitatea dorită:",
            "Ești un asistent AI util și prietenos...",
            height=100
        )
        system_prompt = custom_prompt
    else:
        system_prompt = personality_prompts[personality]
    
    # Parametri model
    st.subheader("🎛️ Parametri Model")
    temperature = st.slider("Creativitate (Temperature):", 0.0, 2.0, 0.7, 0.1)
    max_tokens = st.slider("Lungime răspuns (Max tokens):", 100, 2000, 1000, 100)
    
    # Viteză streaming
    stream_speed = st.slider("Viteză afișare text:", 0.01, 0.5, 0.05, 0.01)
    
    st.divider()
    
    # Statistici conversație
    if "messages" in st.session_state:
        user_msgs = sum(1 for m in st.session_state.messages if m["role"] == "user")
        ai_msgs = sum(1 for m in st.session_state.messages if m["role"] == "assistant")
        st.metric("Mesaje utilizator", user_msgs)
        st.metric("Răspunsuri AI", ai_msgs)
    
    # Butoane acțiuni
    st.divider()
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🗑️ Șterge chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    
    with col2:
        if st.button("💾 Salvează", use_container_width=True):
            if "messages" in st.session_state and st.session_state.messages:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"chat_{timestamp}.txt"
                with open(filename, "w", encoding="utf-8") as f:
                    for msg in st.session_state.messages:
                        if msg["role"] != "system":
                            f.write(f"{msg['role'].upper()}: {msg['content']}\n\n")
                st.success(f"Salvat în {filename}")

# Inițializare state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Afișare istoric mesaje
for message in st.session_state.messages:
    if message["role"] != "system":
        avatar = "🧑‍💻" if message["role"] == "user" else "🤖"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

# Input utilizator
if user_input := st.chat_input("Scrie mesajul tău aici... 💬"):
    # Adaugă mesaj utilizator
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_input)

    # Pregătește mesajele pentru API
    api_messages = [
        {"role": "system", "content": system_prompt}
    ] + st.session_state.messages

    # Generează răspuns AI
    with st.chat_message("assistant", avatar="🤖"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            # Afișează indicator de încărcare
            with st.spinner("🤔 Gândesc..."):
                stream = ollama.chat(
                    model=selected_model,
                    messages=api_messages,
                    stream=True,
                    options={
                        "temperature": temperature,
                        "num_predict": max_tokens
                    }
                )

                # Stream răspuns cu cursor
                for chunk in stream:
                    content = chunk['message']['content']
                    full_response += content
                    response_placeholder.markdown(full_response + "▌")
                    time.sleep(stream_speed)

                # Afișează răspuns final fără cursor
                response_placeholder.markdown(full_response)

            # Salvează răspunsul
            st.session_state.messages.append({
                "role": "assistant",
                "content": full_response
            })

        except Exception as e:
            st.error(f"❌ Eroare Ollama: {str(e)}")
            st.info("💡 Verifică dacă Ollama rulează și dacă modelul este descărcat.")

# Footer
st.divider()
st.markdown(
    "<div style='text-align: center; color: white; padding: 10px;'>"
    "Dezvoltat cu ❤️ folosind Streamlit și Ollama"
    "</div>",
    unsafe_allow_html=True
)
