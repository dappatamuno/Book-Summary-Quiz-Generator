import streamlit as st
from app.summarize import generate_summary
from app.quiz_generator import generate_quiz, evaluate_answers
from app.utils import extract_text_from_file

st.set_page_config(page_title="Book Summary & Quiz", layout="wide")
st.markdown("<style>" + open("app/templates/style.css").read() + "</style>", unsafe_allow_html=True)

st.title("Interactive Book Summary & Quiz Generator")

uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])

if uploaded_file:
    with st.spinner("Processing your file..."):
        full_text = extract_text_from_file(uploaded_file)

        if full_text:
            summary = generate_summary(full_text)
            st.subheader("Summary")
            st.write(summary)

            st.subheader("Quiz")
            quiz = generate_quiz(summary)

            user_answers = []
            for i, q in enumerate(quiz):
                st.markdown(f"**{i+1}. {q['question']}**")
                user_input = st.radio(f"Answer {i+1}", q["options"], key=i)
                user_answers.append(user_input)

            if st.button("Submit Quiz"):
                score, feedback = evaluate_answers(quiz, user_answers)
                st.success(f"You scored {score}/{len(quiz)}")
                for i, f in enumerate(feedback):
                    st.markdown(f"**Q{i+1} Feedback**: {f}")
        else:
            st.error("Unable to extract text. Please try a different file.")
