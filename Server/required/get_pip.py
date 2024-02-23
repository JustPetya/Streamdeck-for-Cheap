import os


class get_pip:
    @staticmethod
    def run_update():
        python = "python3"
        pip = "pip3"
        if os.name in ("nt", "dos"):
            python = "python"
            pip = "pip"
        os.system(python + " -m " + pip + " install --upgrade pip")
        os.system(python + " -m " + pip + " install -r required/required.txt")
