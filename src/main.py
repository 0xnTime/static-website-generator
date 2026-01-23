from copy_contents import setup_directory
from generate_page import generate_pages_recursive

import sys

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"


    print("Copying static files to public directory...")
    setup_directory(dir_path_static, dir_path_public)


    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)



    


main()
