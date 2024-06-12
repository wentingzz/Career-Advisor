import gradio as gr
from cover import cover_letter_app as cover_ui
from career import career_advice_app as career_ui
from resume import resume_polish_application as resume_ui
# Create tabs
tabbed_ui = gr.TabbedInterface(
    interface_list=[career_ui, resume_ui, cover_ui], 
    tab_names=["Consult Advisor", "Polish Resume", "Generate Cover Letter"],
    title="Career Advising App"
)
# Launch the application
tabbed_ui.launch()