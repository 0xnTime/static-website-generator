from block_markdown import markdown_to_html_node
import os


def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            txt = line[2::]
            return txt.strip()
    raise Exception("Md must have a header for title")



def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html_content = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)

    full_html = template.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)
    full_html = full_html.replace('href="/', 'href="{basepath')
    full_html = full_html.replace('src="/', 'src="{basepath}"')

    dirpath = os.path.dirname(dest_path)
    if dirpath != "" and not os.path.exists(dirpath):
        os.makedirs(dirpath)

    with open(dest_path, "w") as f:
        f.write(full_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    files = os.listdir(dir_path_content)

    for file in files:
        src_path = os.path.join(dir_path_content, file)
        if os.path.isdir(src_path):
            dest_subdir = os.path.join(dest_dir_path, file)
            if not os.path.exists(dest_subdir):
                os.mkdir(dest_subdir)
            generate_pages_recursive(src_path, template_path, dest_subdir, basepath)
        if os.path.isfile(src_path):
            if file.endswith(".md"):
                name, ext = file.split(".")
                html_name = name + ".html"
                dest_path = os.path.join(dest_dir_path, html_name)
                generate_page(src_path, template_path, dest_path, basepath)
