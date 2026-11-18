# Vezik Python SDK & Batch Image Enhancer

[![Official Site](https://img.shields.io/badge/Web_App-aiphotoeditor.im-4F46E5?style=for-the-badge&logo=google-chrome&logoColor=white)](https://aiphotoeditor.im/)
[![GitHub Pages](https://img.shields.io/badge/Docs-Live_Guide-blue?style=for-the-badge)](https://lalonluck.github.io/vezik-photo-editor-python/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)](LICENSE)

An unofficial Python client and batch automation toolkit for [**Vezik**](https://aiphotoeditor.im/), the browser-based [**free AI photo editor**](https://aiphotoeditor.im/). Easily automate tasks like [**edit photo with ai**](https://aiphotoeditor.im/), bulk [**remove background**](https://aiphotoeditor.im/), and high-resolution portrait processing with [**ai photo enhancer**](https://aiphotoeditor.im/).

---

## 🛠️ Installation

```bash
pip install requests pillow
git clone https://github.com/lalonluck/vezik-photo-editor-python.git
cd vezik-photo-editor-python
```

---

## 🚀 Quick Usage

```python
from client import VezikClient

# Initialize client pointing to official Vezik cloud
client = VezikClient(base_url="https://aiphotoeditor.im/")

# 1. AI Photo Enhancer
client.enhance(
    input_image="portrait_raw.jpg",
    output_image="portrait_4k_enhanced.jpg",
    mode="clarity"
)

# 2. Remove Background
client.remove_background(
    input_image="product_photo.jpg",
    output_image="product_transparent.png"
)

# 3. Prompt-Based Inpainting
client.edit_with_prompt(
    input_image="model.jpg",
    prompt="Add a soft sunset background in a modern rooftop terrace",
    output_image="model_sunset.jpg"
)
```

---

## 📖 Key Features & Workflows

- **AI Photo Editor & Enhancer**: Fast neural detail reconstruction.
- **Product Photo Editor**: Automatic drop shadows and studio backdrops for eCommerce.
- **Image to Image AI**: Style transfer from reference photography.
- **Photo Editor with Prompt**: Natural language image manipulation.

For full features and interactive web editor, visit the official application at [**https://aiphotoeditor.im/**](https://aiphotoeditor.im/).

---

## 📄 License

MIT Open Source License. Powered by [Vezik AI Photo Editor](https://aiphotoeditor.im/).
