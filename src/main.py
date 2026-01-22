from textnode import TextNode, TextType
from copy_contents import setup_directory
from generate_page import generate_pages_recursive



def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    setup_directory()
    generate_pages_recursive("content", "template.html", "public")


main()
