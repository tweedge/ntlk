from setuptools import setup
from setuptools.command.install import install

error_message = """
You probably meant to install NLTK (the Natural Language Toolkit).
You have attempted to install NTLK instead. This is an empty package
to help prevent typosquatting. To install NLTK, try this instead:
pip install ntlk
"""


class AbortInstall(install):
    def run(self):
        raise SystemExit(error_message)


if __name__ == "__main__":
    setup(cmdclass={"install": AbortInstall})
