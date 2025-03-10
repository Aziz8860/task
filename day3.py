import streamlit as st

st.title("Notetaking App")
st.write("Welcome to my notetaking app!")

# Initialize session state for storing notes
if "notes" not in st.session_state:
    st.session_state.notes = []

note = st.text_area("Take a note")
date = st.date_input("Date")

submit_btn = st.button("Save")

# Save note when button is clicked
if submit_btn and note:
    st.session_state.notes.append({"note": note, "version": version, "date": date})

st.write("### Saved Notes:")
for i, saved_note in enumerate(st.session_state.notes, 1):
    st.write(f"**{i}. Note:** {saved_note['note']}")
    st.write(f"**Date:** {saved_note['date']}")
    st.write("---")