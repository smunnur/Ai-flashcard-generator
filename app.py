import streamlit as st
# import openai   # No need for OpenAI in demo mode

# --- CONFIG ---
st.set_page_config(page_title="AI Flashcard Generator", page_icon="📚", layout="centered")

# --- APP TITLE ---
st.title("📚 AI Flashcard Generator")
st.write("Paste your text below, and AI will generate flashcards (Q&A format).")

# --- INPUT FIELD ---
user_text = st.text_area("Enter your notes, article, or text:", height=200)

# --- GENERATE FLASHCARDS ---
if st.button("Generate Flashcards"):
    if not user_text.strip():
        st.error("Please enter some text to generate flashcards.")
    else:
        try:
            # --- DEMO MODE: generate sample flashcards ---
            flashcards = """
Q: What is the main role of a Jr. Security Engineer?
A: To understand and implement electronic security systems such as ACS, IDS, and CCTV.

Q: What are some responsibilities of the Jr. Security Engineer?
A: Reviewing floor plans, designing solutions, creating BOMs, and assisting with RFI/RFP responses.

Q: What qualifications are preferred for this role?
A: Mechanical/Engineering degree or 2+ years of experience, knowledge of MEP systems, strong problem-solving and communication skills.

Q: Name some software tools mentioned in the job description.
A: Microsoft Office, Excel, Adobe, Microsoft Project, Visio, BlueBeam, AutoCAD, Revit.
"""

            st.subheader("✨ Generated Flashcards")
            st.write(flashcards)

            # --- DOWNLOAD OPTION ---
            st.download_button("Download Flashcards", flashcards, file_name="flashcards.txt")

        except Exception as e:
            st.error(f"Error: {str(e)}")
