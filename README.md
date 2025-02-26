---
tags: [gradio-custom-component, Number]
title: gradio_folium
short_description: A gradio custom component
colorFrom: blue
colorTo: yellow
sdk: gradio
pinned: false
app_file: space.py
---

# `gradio_folium`
<a href="https://pypi.org/project/gradio_folium/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_folium"></a>  

Python library for easily interacting with trained machine learning models

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

## `Folium`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
typing.Any
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>height</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>container</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>load_fn</code></td>
<td align="left" style="width: 25%;">

```python
typing.Optional[typing.Callable[..., typing.Any]][
    typing.Callable[..., typing.Any][Ellipsis, typing.Any],
    None,
]
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>
</tbody></table>




### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Should return, the output data received by the component from the user's function in the backend.

 ```python
 def predict(
     value: Unknown
 ) -> folium.folium.Map:
     return value
 ```
 
