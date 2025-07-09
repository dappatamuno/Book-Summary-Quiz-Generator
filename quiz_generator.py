from langchain.llms import OpenAI

def generate_quiz(summary):
    prompt = f"Based on the following summary, generate 5 multiple-choice questions that test reading comprehension. Include 4 answer options and indicate the correct one. Provide short feedback for each question.\n\n{summary}"
    llm = OpenAI(model_name="gpt-4")
    result = llm(prompt)
    # Ideally parse the result into a list of dicts with 'question', 'options', 'answer', 'explanation'
    return [
        {
            "question": "Placeholder Q1?",
            "options": ["A", "B", "C", "D"],
            "answer": "A",
            "explanation": "Explanation 1"
        }
    ]

def evaluate_answers(quiz, user_answers):
    score = 0
    feedback = []
    for i, (q, ua) in enumerate(zip(quiz, user_answers)):
        if ua == q["answer"]:
            score += 1
            feedback.append("Correct! " + q["explanation"])
        else:
            feedback.append(f"Wrong. Correct answer: {q['answer']}. {q['explanation']}")
    return score, feedback
