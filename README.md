# Affirmative Sampling: Reference Implementation

[![pytest](https://github.com/jlumbroso/affirmative-sampling/actions/workflows/continuous-integration.yaml/badge.svg)](https://github.com/jlumbroso/affirmative-sampling/actions/workflows/continuous-integration.yaml)
[![codecov](https://codecov.io/gh/jlumbroso/affirmative-sampling/branch/main/graph/badge.svg?token=4S8TD999YC)](https://codecov.io/gh/jlumbroso/affirmative-sampling)

This repository contains a reference implementation, in Python, of the _Affirmative Sampling_ algorithm by Jérémie Lumbroso and Conrado Martínez (2022), as well as the original paper, accepted at the Analysis of Algorithms 2022 edition in Philadelphia.

## Abstract

_Affirmative Sampling_ is a practical and efficient novel algorithm to obtain random samples of distinct elements from a data stream.

Its most salient feature is that the size $S$ of the sample will, on expectation, **grow with the (unknown) number $n$ of distinct elements in the data stream**.

As any distinct element has the same probability to be sampled, and the sample size is greater when the "diversity" (the number of distinct elements) is greater, the samples that _Affirmative Sampling_ delivers are more representative than those produced by any scheme where the sample size is fixed _a priori_—hence its name. This repository contains a reference implementation, in Python, to illustrate how the algorithm works and showcase some basic experimentation.

## Installation

This package is available on PyPI and can be installed through the typical means:

```shell
$ pip install affirmative_sampling
```

The hash functions that are used in this package come from [the `randomhash` Python package](https://github.com/jlumbroso/python-random-hash).

## Historical Context

Sampling is a very important tool, because it makes it possible to infer information about a large data set using the characteristics of a much smaller data set. Historically, it came in the following flavors:

- **(Straight) Sampling**: Each element of the initial data set of size $N$ is taken with the same (fixed) probability $p$. Such sample's size is a random variable, distributed like a binomial and centered in a mean of $Np$.

- **Reservoir Sampling**: This (family of) algorithm(s), [introduced by Jeffrey Vitter (1985)](https://doi.org/10.1145/3147.3165), ensures the size of the resulting sample is fixed, by using _replacements_—indeed an element that is in the sample at some point in these algorithms, might later be evicted and replaced, to ensure the sample is both of fixed size, yet contains elements with uniform probability.

- **Adaptive/Distinct Sampling**: This algorithm, introduced by Mark Wegman (1980), [analyzed by Philippe Flajolet (1990)](https://doi.org/10.1007/BF02241657) and [rebranded by Philip Gibbons (2001)](http://www.vldb.org/conf/2001/P541.pdf), draws elements not from a data set of size $N$, but by the underlying set of distinct items of that data set, of cardinality $n$. Both previous families of algorithm are susceptible to large, frequent elements, that drawn out other more rare elements. Distinct sampling algorithms are family of sampling algorithms that use hash functions to be insensitive to repetitions. While the size of the sample is not fixed, it oscillates closely around a fixed (constant) size.

- **Affirmative Sampling**: This novel algorithm conserves the properties of the Distinct Sampling family of algorithms (because it also uses a hash function to be insensitive to repeated elements), but allows the target size of the sample to be a function of $n$, the number of distinct elements in the source data set—to be precise, the size of the sample is supposed to be $~k \cdot \log \frac n k + k$, logarithmic in the number of distinct elements. This is important, because the accuracy of estimates inferred from a random sample depend on how representative the sample is of the diversity of the source data set, and Affirmative Sampling calibrates the size of the sample to deliver accurate estimates.

## Intuition of How the Sample Grows

The novel property of the algorithm is that it grows in a controlled way, that is related to the logarithm of the number of distinct elements. The sample is divided into two parts: A fixed-size part (`sample_core`) that will always be of size $k$; and a variable-size part (`sample_xtra`) that will grow slowly throughout the process of the algorithm. Depending on its hashed value, a new element $z$ might either be DISCARDED, REPLACE an existing element of the sample, or EXPAND the variable-size sample, see diagram below:

```
REPRESENTATION OF THE SAMPLE DURING THE ALGORITHM         |   OUTCOMES FOR NEW ELEMENT z
                                                          |         y = hash(z)
      High hash values                                    |
             ^                                            |
             |                                            |
             |                                            |
+-------------------------+ <-- max hash of S so far      |
|                         |     (no need to track this)   | <-- y >= k-th hash
| sample_core             |                               |
| size = k (always/fixed) |                               |  EXPAND:
|                         |                               |    ADD z to sample_core
+-------------------------+ <-- k-th hash of S            |    MOVE z_kth_hash from
|                         |     = min hash in sample_core |      sample_core to sample_xtra
|                         |                               |    total size ++
| sample_xtra             |                               |
| size = S - k (variable) |                               | <-- kth_hash > y > min_hash
|                         |                               |
|                         |                               |  REPLACE z_min_hash with z:
|                         |                               |    ADD z to sample_xtra
+-------------------------+ <-- min hash of S             |    REMOVE z_min_hash from sample_xtra
             |                  = min hash in sample_xtra |
             |                                            | <-- y <= min_hash
             |                                            |
             v                                            |  DISCARD z
       Low hash values                                    |
                                                          |
```

As the paper illustrates, it is also possible to design variants of the Affirmative Sampling algorithm, with a growth rate that is different than logarithmic.

## License

This project is licensed under the MIT license, which means that you can do whatever you want with this code, as long as you preserve, in some form, the associated copyright and license notice.
