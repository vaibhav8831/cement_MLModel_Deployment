import gradio as gr
import pickle
import numpy as np

# Load the trained model
with open("pickle.pkl", "rb") as file:
    model = pickle.load(file)


# Prediction function
def prediction(cement):
    features = np.array([[cement]])
    result = model.predict(features)

    return f"Predicted class: {result[0]}"


# Create Gradio interface
demo = gr.Interface(
    fn=prediction,
    inputs=gr.Number(
        label="Cement (component 1) (kg in a m³ mixture)"
    ),
    outputs=gr.Textbox(
        label="Prediction"
    ),
    title="Machine Learning Gradio Model",
    description="Enter the cement quantity to get the model prediction."
)


# Launch the app
if __name__ == "__main__":
    demo.launch()