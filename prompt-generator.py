import os
import json
from openai import OpenAI
import streamlit as st

# Load configuration from JSON file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Extract prompt from the configuration
TEXT_OUTPUT_PROMPT = config["text_meta_prompt"].strip()
AUDIO_OUTPUT_PROMPT = config["audio_meta_prompt"].strip()

client = OpenAI()
openai_api_key = os.environ.get('OPENAI_API_KEY')

st.set_page_config(layout="wide", page_title="Prompt Generator")
st.markdown("## Prompt Generator")
st.markdown("### Generate the perfect prompt for your AI model")

def generate_response(meta_prompt, task_or_prompt, model):
    completion = client.chat.completions.create(
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

    return completion.choices[0].message.content

def update_meta_prompt():
    st.session_state["selected_meta_prompt"] = TEXT_OUTPUT_PROMPT if st.session_state["selected_option"] == 'Text prompt' else AUDIO_OUTPUT_PROMPT

# Place the radio button outside the form to avoid the Streamlit error, as a change state method is triggered
selected_option = st.radio("Choose the output format:", ['Text prompt', 'Audio prompt'], key="selected_option", on_change=update_meta_prompt)
update_meta_prompt()

with st.form('my_form'):
    open_ai_model = st.selectbox('Which OpenAI model should we use?', ('gpt-4o', 'gpt-4o-mini', 'o1-preview', 'o1-mini'))

    # Adjust chosen_meta_prompt based on session state logic
    chosen_meta_prompt = st.text_area('Meta Prompt:', value=st.session_state["selected_meta_prompt"], height=400)  # Initial value can be empty
    task_goal_or_prompt = st.text_area('Task, Goal or Prompt:', value="", height=300)

    submitted = st.form_submit_button('Generate')
    if submitted:
        with st.spinner('Generating LLM response...'):
            st.info(generate_response(chosen_meta_prompt, task_goal_or_prompt, open_ai_model))
