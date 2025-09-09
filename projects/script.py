import os

def fix_readme_extensions(root_dir):
    for entry in os.listdir(root_dir):
        subdir = os.path.join(root_dir, entry)
        if os.path.isdir(subdir):
            readme_path = os.path.join(subdir, "README")
            readme_md_path = os.path.join(subdir, "README.md")
            if os.path.isfile(readme_path):
                if not os.path.exists(readme_md_path):
                    os.rename(readme_path, readme_md_path)
                    print(f"Renamed: {readme_path} -> {readme_md_path}")
                else:
                    print(f"Skipped (README.md already exists): {readme_md_path}")

if __name__ == "__main__":
    root = os.path.dirname(os.path.abspath(__file__))
    fix_readme_extensions(root)