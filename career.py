# Import necessary packages
from ibm_watson_machine_learning.foundation_models import Model
import gradio as gr

# Model and project settings
model_id = "meta-llama/llama-2-70b-chat"  # Directly specifying the LLAMA2 model

# Set credentials
my_credentials = {
    "url": "https://us-south.ml.cloud.ibm.com"
}

# Generation parameters
gen_parms = {
    "max_new_tokens": 1024,  # Adjust as needed
    "temperature": 0.7  # Adjust for creativity
}

project_id = "skills-network"  # Use this project_id
space_id = None
verify = False

# Initialize the model with the correct parameters
model = Model(model_id, my_credentials, gen_parms, project_id, space_id, verify)

# Function to generate career advice
def generate_career_advice(position_applied, job_description, resume_content):
    # The prompt for the model
    prompt = f"Considering the job description: {job_description}, and the resume provided: {resume_content}, identify areas for enhancement in the resume. Offer specific suggestions on how to improve these aspects to better match the job requirements and increase the likelihood of being selected for the position of {position_applied}."
    
    # Generate response
    generated_response = model.generate(prompt, gen_parms)
    
    # Extract and format the generated text
    advice = generated_response["results"][0]["generated_text"]
    return advice

# Create Gradio interface for the career advice application
career_advice_app = gr.Interface(
    fn=generate_career_advice,
    allow_flagging="never", # Deactivate the flag function in gradio as it is not needed.
    inputs=[
        gr.Textbox(label="Position Applied For", placeholder="Enter the position you are applying for..."),
        gr.Textbox(label="Job Description Information", placeholder="Paste the job description here...", lines=10),
        gr.Textbox(label="Your Resume Content", placeholder="Paste your resume content here...", lines=10),
    ],
    outputs=gr.Textbox(label="Advice"),
    title="Consult Advisor",
    description="Enter the position you're applying for, paste the job description, and your resume content to get advice on what to improve for getting this job."
)

# Launch the application