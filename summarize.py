from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

def generate_summary(text):
    prompt = PromptTemplate.from_template(
        'Summarize the following text clearly and concisely in 4-6 paragraphs for general readers:\n\n{text}'
    )
    llm = OpenAI(model_name="gpt-4")
    return llm(prompt.format(text=text))
