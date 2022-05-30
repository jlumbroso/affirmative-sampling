"""
A reference implementation of the Affirmative Sampling algorithm as
described in:

Lumbroso, Jéremie, and Conrado, Martínez. "Affirmative Sampling:
    Theory and Applications." In 32nd International Conference on Probabilistic,
    Combinatorial and Asymptotic Methods for the Analysis of Algorithms (AofA 2022).
    Schloss Dagstuhl—Leibniz-Zentrum fuer Informatik, 2022.
"""

__version__ = "0.1.0"
__author__ = "Jérémie Lumbroso <lumbroso@cs.princeton.edu>"

version_info = tuple(int(v) if v.isdigit()
                     else v for v in __version__.split('.'))
