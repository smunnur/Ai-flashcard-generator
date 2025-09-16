import streamlit as st
import openai

# --- CONFIG ---
st.set_page_config(page_title="AI Flashcard Generator", page_icon="📚", layout="centered")

# --- APP TITLE ---
st.title("📚 AI Flashcard Generator")
st.write("Paste your text below, and AI will generate flashcards (Q&A format).")

# --- INPUT FIELD ---
user_text = st.text_area("Enter your notes, article, or text:", height=200)

# --- API KEY INPUT (hidden for deployment you can use st.secrets) ---
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

# --- GENERATE FLASHCARDS ---
if st.button("Generate Flashcards"):
    if not api_key:
        st.error("Please enter your OpenAI API key.")
    elif not user_text.strip():
        st.error("Please enter some text to generate flashcards.")
    else:
        try:
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an assistant that generates study flashcards in Q&A format."},
                    {"role": "user", "content": f"Generate concise flashcards (Question and Answer pairs) from the following text:\n\n{user_text}"}
                ],
                temperature=0.5,
                max_tokens=600
            )
            flashcards = response["choices"][0]["message"]["content"]
            st.subheader("✨ Generated Flashcards")
            st.write(flashcards)

            # --- DOWNLOAD OPTION ---
            st.download_button("Download Flashcards", flashcards, file_name="flashcards.txt")
        
        except Exception as e:
            st.error(f"Error: {str(e)}")
