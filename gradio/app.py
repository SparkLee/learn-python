import gradio as gr


def greet(name):
    return "Hello " + name+"!"


demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="请输入您的想法：",
    description="想要啥，你就说啥！",
    # theme=gr.themes.Monochrome(),
    # css=".gradio-container {background-color: black}"
)
demo.launch()
