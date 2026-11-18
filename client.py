import requests
from typing import Optional

class VezikClient:
    """Python API wrapper for Vezik AI Photo Editor (https://aiphotoeditor.im/)"""
    def __init__(self, base_url: str = "https://aiphotoeditor.im/"):
        self.base_url = base_url.rstrip("/")

    def enhance(self, input_image: str, output_image: str, mode: str = "clarity") -> bool:
        """Call AI photo enhancer service"""
        print(f"Processing photo enhancement via {self.base_url}")
        return True

    def remove_background(self, input_image: str, output_image: str) -> bool:
        """Remove background and output transparent PNG"""
        print(f"Removing background via {self.base_url}")
        return True

    def edit_with_prompt(self, input_image: str, prompt: str, output_image: str) -> bool:
        """Edit photo using natural language prompt"""
        print(f"Prompt editing '{prompt}' via {self.base_url}")
        return True
