# ntlk

[![License](https://img.shields.io/github/license/tweedge/ntlk)](https://github.com/tweedge/ntlk)
![Downloads](https://img.shields.io/pypi/dm/ntlk?style=plastic)
[![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
[![Linted](https://img.shields.io/badge/also%20passes-flake8-blue.svg)](https://github.com/PyCQA/flake8)
[![Made By Me](https://img.shields.io/badge/made%20by-some%20idiot-red.svg)](https://chris.partridge.tech/)

Today, I was a fuckwit. While doing a demo on a call, I attempted to install NLTK with `pip install ntlk` three separate times, receiving an error "No matching distribution found for ntlk." I stalled, Googling to see if the [Natural Language Toolkit](https://www.nltk.org/) was compatible with my version of Python and making sure that PyPI was online before realizing I'd typed in the name wrong. I fell victim to one of the classic blunders: ~~never get involved in a land war in Asia~~ ~~never go in against a Sicilian when death is on the line~~ typos (especially during demos, as demos are cursed).

I'm not the first to fall prey to this typo - as of writing, there are 244 results on StackOverflow for NTLK, just over 1% of the 21,228 results for NLTK. It feels like there's a deeper reason for this prevalence as well - I don't know *why* N-T-L-K sounds so much better to my mind, but even after realizing this error, I still alternate between typing and saying N-T-L-K and N-L-T-K. Why does my mind prefer NTLK? Is the COVID vaccine running Windows NT in my head? More likely there's some linguistic preference thing that I'm not aware of, but if anyone has ideas, drop them in an Issue against this project's [GitHub repository](https://github.com/tweedge/ntlk/issues).

## What is This?

Inspired by other anti-typosquatting packages, such as [pylola/requirements.txt](https://github.com/pylola/requirements.txt), this package is a safeguard against running `pip install ntlk`, and will provide you with the correct spelling of N-L-T-K:

```
$ pip install ntlk
Collecting ntlk
Building wheels for collected packages: ntlk
  Building wheel for ntlk (setup.py) ... error
  Complete output (10 lines):
  running bdist_wheel
  running build
  installing to build/bdist.linux-x86_64/wheel
  running install

  You probably meant to install NLTK (the Natural Language Toolkit).
  You have attempted to install NTLK instead. This is an empty package
  to help prevent typosquatting. To install NLTK, try this instead:
  pip install nltk
  
  Stay safe,
  tweedge <3
```

## Why Bother?

The reason I felt it important to create this package was because a. my failure could save you some time and b. typosquatting is a hilariously potent issue for people using package managers - including PyPI (ref: [lwn](https://lwn.net/Articles/834078/)). pip installs download code directly to your machine to be executed as your user (even during install, before you try using it) - if you downloaded a fake NLTK package, would a bad actor have been able to exfiltrate data from your workstation? Would you have pinned it into your repository? Would you have even noticed that you had N-T-L-K installed, since your IDE would happily suggest N-T-L-K when you're typing and correcting things? Who's to say.

But hey, at least you won't be bitten by this *exact* typo anymore, thanks to my dumbassery.

Are there other packages you've misspelled frequently? Shoot me an email if you want me to sit on another package - it's in [setup.cfg](https://github.com/tweedge/ntlk/blob/main/setup.cfg) - or fork and create your own.