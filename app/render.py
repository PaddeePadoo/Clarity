# app/render.py
import markdown

def render_markdown_to_html(markdown_content: str) -> str:
    """Convert markdown text to HTML."""
    return markdown.markdown(markdown_content)
