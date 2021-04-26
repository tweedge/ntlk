# ntlk

[![License](https://img.shields.io/github/license/tweedge/ntlk)](https://github.com/tweedge/ntlk)
[![Downloads](https://img.shields.io/pypi/dm/ntlk)](https://pypi.org/project/ntlk/)
[![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
[![Linted](https://img.shields.io/badge/also%20passes-flake8-blue.svg)](https://github.com/PyCQA/flake8)
[![Made By Me](https://img.shields.io/badge/made%20by-some%20nerd-red.svg)](https://chris.partridge.tech/)

While doing a demo on a call, I attempted to install NLTK with `pip install ntlk` three separate times, receiving an error "No matching distribution found for ntlk." I stalled, Googling to see if the [Natural Language Toolkit](https://www.nltk.org/) was compatible with my version of Python and making sure that PyPI was online before realizing I'd typed in the name wrong. I fell victim to one of the classic blunders:
* ~~Never get involved in a land war in Asia~~
* ~~Never go in against a Sicilian when death is on the line~~
* Doing a live demo. Somehow, something usually goes wrong.

WHat's more interesting is: I'm not the first to fall prey to this typo. I'm in a very significant minority of NLTK-typoers. As of writing, there are 244 results on StackOverflow for NTLK, just over 1% of the 21,228 results for NLTK. This is a massive quantity of typos! Someone has to do something!

## What is This?

Inspired by other anti-typosquatting packages, such as [pylola/requirements.txt](https://github.com/pylola/requirements.txt), this package is a safeguard against running `pip install ntlk`, and provides you with the correct spelling of N-L-T-K:

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

This also fires a request to [https://package.mouseparty.org](https://package.mouseparty.org) before the install fails and that message is displayed. This discloses what package and version was downloaded from PyPI. This enables me to track the spread and prevalence of this issue more accurately and do cool research like finding out if people are more likely to make this typo when sleepy late-at-night or busy during working hours. As this is privacy-prioritizing research, no system information is collected.

## Why Bother?

The reason I felt it important to create this package was because:
* My failure could save you some time
* Typosquatting is a hilariously potent issue for people using contemporary package managers ([including PyPI](https://lwn.net/Articles/834078/))

To quickly elaborate on why this is a massive problem for developer security: while all contemporary package managers have a way to ensure that the integrity of the package you wanted is good, they can't tell whether or not you mistyped a package during the *initial install*. Further, package managers are rarely sandboxed or contained, especially during development phases at many companies. So the risk to an application may not be as high - you should be using pinned/locked packages that are known to work and be good - but if a mistyped package is malicious, it's about to be running code on your system with your user's privileges. This happens *even before the install completes*, so the window you have to stop an infection after a typo is low *unless there is no malicious package to install in the first place*.

There's much work happening in this space and I want to specifically applaud package managers' management teams for stepping up their security efforts to detect and remove malicious packages faster. That'll never be 100% perfect, but no solution (yet identified) will - in the future, I look forward to more user-friendly and on-by-default sandboxing methodologies rolling out across the industry, which may help mitigate the risk we've observed here.

But at least you won't be bitten by this *exact* typo anymore. I'm also starting up some additional research in this space to typosquat more critical packages. I hopt to have some cool announcements to add to this soon.

Interested in helping out? Shoot me an email - it's in [setup.cfg](https://github.com/tweedge/ntlk/blob/main/setup.cfg) - or fork and start your own research!