# Static Site Generator – Tolkien Blog

A tiny static site generator written in Python. It converts Markdown content in the `content/` directory into HTML pages in the `public/` directory, and copies static assets like CSS and images from `static/`.

The example site is a Tolkien-themed blog with posts about Glorfindel, Tom Bombadil, and _The Lord of the Rings_, plus a contact page.

---

## Project Structure

```txt
.
├── content/
│   ├── blog/
│   │   ├── glorfindel/
│   │   │   └── index.md
│   │   ├── majesty/
│   │   │   └── index.md
│   │   └── tom/
│   │       └── index.md
│   ├── contact/
│   │   └── index.md
│   └── index.md        # Home page markdown
├── static/
│   ├── images/
│   │   ├── glorfindel.png
│   │   ├── rivendell.png
│   │   ├── tolkien.png
│   │   └── tom.png
│   └── index.css
├── src/
│   ├── copystatic.py
│   ├── gencontent.py
│   ├── htmlnode.py
│   ├── inline_markdown.py
│   ├── markdown_blocks.py
│   ├── textnode.py
│   └── main.py
├── template.html
└── public/              # Generated output (created by the generator)
