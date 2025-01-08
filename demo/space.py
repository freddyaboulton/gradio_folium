
import gradio as gr
from app import demo as app
import os

_docs = {'Folium': {'description': 'A base class for defining methods that all input/output components should have.', 'members': {'__init__': {'value': {'type': 'typing.Any', 'default': 'None', 'description': None}, 'height': {'type': 'int | None', 'default': 'None', 'description': None}, 'label': {'type': 'str | None', 'default': 'None', 'description': None}, 'container': {'type': 'bool', 'default': 'True', 'description': None}, 'scale': {'type': 'int | None', 'default': 'None', 'description': None}, 'min_width': {'type': 'int | None', 'default': 'None', 'description': None}, 'visible': {'type': 'bool', 'default': 'True', 'description': None}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': None}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': None}, 'render': {'type': 'bool', 'default': 'True', 'description': None}, 'load_fn': {'type': 'typing.Optional[typing.Callable[..., typing.Any]][\n    typing.Callable[..., typing.Any][Ellipsis, typing.Any],\n    None,\n]', 'default': 'None', 'description': None}, 'every': {'type': 'float | None', 'default': 'None', 'description': None}}, 'postprocess': {'value': {'type': 'folium.folium.Map', 'description': "The output data received by the component from the user's function in the backend."}}, 'preprocess': {}}, 'events': {}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'Folium': []}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_folium`

<div style="display: flex; gap: 7px;">
<a href="https://pypi.org/project/gradio_folium/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_folium"></a>  
</div>

Python library for easily interacting with trained machine learning models
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_folium
```

## Usage

```python

import gradio as gr
from gradio_folium import Folium
from folium import Map
import pandas as pd
import pathlib

df = pd.read_csv(pathlib.Path(__file__).parent / "cities.csv")

def select(df, data: gr.SelectData):
    row = df.iloc[data.index[0], :]
    return Map(location=[row['Latitude'], row['Longitude']])

with gr.Blocks() as demo:
    gr.Markdown(("# 🗺️ Explore World Capitals with Gradio and Folium\n"
                 "Install this custom component with `pip install gradio_folium`"))
    map = Folium(value=Map(location=[25.7617, -80.1918]))
    data = gr.DataFrame(value=df)
    data.select(select, data, map)

if __name__ == "__main__":
    demo.launch()

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `Folium`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["Folium"]["members"]["__init__"], linkify=[])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As output:** Should return, the output data received by the component from the user's function in the backend.

 ```python
def predict(
    value: Unknown
) -> folium.folium.Map:
    return value
```
""", elem_classes=["md-custom", "Folium-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          Folium: [], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
