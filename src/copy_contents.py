import shutil
import os


def setup_directory(dir_path_static, dir_path_public):

    if not os.path.exists(dir_path_public):
        os.mkdir(dir_path_public)
    else:
        shutil.rmtree(dir_path_public)
        os.mkdir(dir_path_public)

    copy_contents(dir_path_static,dir_path_public)


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
