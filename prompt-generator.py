import os
import json
from openai import OpenAI
import streamlit as st

# instructions
# Store your OpenAI key in env var OPENAI_API_KEY
# pip install openai langchain streamlit
# streamlit run prompt-generator.py

# Load configuration from JSON file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Extract prompt from the configuration
TEXT_OUTPUT_PROMPT = config["text_meta_prompt"].strip()
AUDIO_OUTPUT_PROMPT = config["audio_meta_prompt"].strip()

client = OpenAI()
openai_api_key = os.environ.get('OPENAI_API_KEY')

st.set_page_config(layout="centered", page_title="Prompt Generator")
st.markdown("## Generate the perfect prompt for your AI model")
st.markdown("### Personalized stories for the masses")

def generate_response(meta_prompt, task_or_prompt, model):
    return client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": meta_prompt,
            },
            {
                "role": "user",
                "content": "Task, Goal, or Current Prompt:\n" + task_or_prompt,
            },
        ],
    )

with st.form('my_form'):
    open_ai_model = st.selectbox('Which OpenAI model should we use?', ('gpt-4o', 'gpt-4o-mini', 'o1-preview', 'o1-mini'))
    selected_option = st.radio("Choose the output format:", ['Text prompt', 'Audio prompt'])

    selected_meta_prompt = TEXT_OUTPUT_PROMPT if selected_option == 'Text prompt' else AUDIO_OUTPUT_PROMPT
    chosen_meta_prompt = st.text_area('Meta Prompt:', value=selected_meta_prompt, height=220)
    task_goal_or_prompt = st.text_area('Task, Goal or Prompt:', value="", height=400)

    submitted = st.form_submit_button('Generate')
    if submitted:
        with st.spinner('Generating LLM response...'):
            st.info(generate_response(chosen_meta_prompt, task_goal_or_prompt, open_ai_model).content)