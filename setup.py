from setuptools import setup
from setuptools.command.install import install

error_message = """
You probably meant to install NLTK (the Natural Language Toolkit).
You have attempted to install NTLK instead. This is an empty package
to help prevent typosquatting. To install NLTK, try this instead:
pip install nltk

Stay safe,
tweedge <3
"""


class AbortInstall(install):
    def run(self):
        # To track the spread of this issue, a web request is sent
        # This endpoint takes a small amount of data from headers of POSTs
        url = "https://package.mouseparty.org/"
        
        try:
            # Python3-compatible urllib setup
            from urllib.request import Request, urlopen
            req = Request(url, method="POST")
        except ImportError:
            # Python2-compatible urllib setup
            from urllib2 import Request, urlopen
            req = Request(url, data="python2=bad")

        try:
            # Please note that no system data is collected
            req.add_header("Packager", "pip")
            req.add_header("Package", "ntlk")
            req.add_header("Package_Version", "1.0.3")
            req.add_header("Report_Version", "1")

            # Here, the report is sent, but we don't care about the read data
            urlopen(req).read()
        except Exception:
            # If an error happens or this is not possible, OK, whatever
            pass

        # And a message explaining the issue is raised
        raise SystemExit(error_message)


if __name__ == "__main__":
    setup(cmdclass={"install": AbortInstall})
