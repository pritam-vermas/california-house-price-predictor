import gradio as gr
import joblib
import pandas as pd

# Load saved model
model = joblib.load("iris_model.pkl")

# Prediction function
def predict_flower(sepal_length, sepal_width, petal_length, petal_width):

    sample = pd.DataFrame({
        "sepal_length": [sepal_length],
        "sepal_width": [sepal_width],
        "petal_length": [petal_length],
        "petal_width": [petal_width]
    })

    prediction = model.predict(sample)

    return prediction[0]


# UI
demo = gr.Interface(
    fn=predict_flower,
    inputs=[
        gr.Number(label="Sepal Length"),
        gr.Number(label="Sepal Width"),
        gr.Number(label="Petal Length"),
        gr.Number(label="Petal Width")
    ],
    outputs=gr.Textbox(label="Predicted Species"),
    title="🌸 Iris Flower Classification",
    description="Enter flower measurements to predict the species."
)

demo.launch()
