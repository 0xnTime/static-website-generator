import shutil
import os


def setup_directory():
    curr = os.getcwd()
    destination_directory = os.path.join(curr, "public/")
    source_dir = os.path.join(curr, "static")
    if not os.path.exists(destination_directory):
        os.mkdir(destination_directory)
    else:
        shutil.rmtree(destination_directory)
        os.mkdir(destination_directory)

    copy_contents(source_dir,destination_directory)


def copy_contents(source_dir, dest_dir):

    for item in os.listdir(source_dir):
        src_path = os.path.join(source_dir,item)
        dst_path = os.path.join(dest_dir, item)
        if os.path.isdir(src_path):
            os.mkdir(dst_path)
            print(f"copied {src_path}, {dst_path}")
            copy_contents(src_path,dst_path)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
