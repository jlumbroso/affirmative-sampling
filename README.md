# Affirmative Sampling: Reference Implementation

This repository contains a reference implementation, in Python, of the _Affirmative Sampling_ algorithm by Jérémie Lumbroso and Conrado Martínez (2022).

## Abstract

_Affirmative Sampling_ is a practical and efficient novel algorithm to obtain random samples of distinct elements from a data stream.

Its most salient feature is that the size $S$ of the sample will, on expectation, **grow with the (unknown) number $n$ of distinct elements in the data stream**.

As any distinct element has the same probability to be sampled, and the sample size is greater when the "diversity" (the number of distinct elements) is greater, the samples that _Affirmative Sampling_ delivers are more representative than those produced by any scheme where the sample size is fixed _a priori_—hence its name.

This repository contains a reference implementation, in Python, to illustrate how the algorithm works and showcase some basic experimentation.

## Context

## Intuition

```
REPRESENTATION OF THE SAMPLE DURING THE ALGORITHM                  |   POSSIBLE OUTCOMES FOR A NEW ELEMENT y = hash(z)
                                                                   |
      High hash values                                             |
             ^                                                     |
             |                                                     |
             |                                                     |
+-------------------------+  <-- max hash so far                   |
|                         |      (no need to keep/compute this)    |
| sample_core             |                                        |   <-- y >= k-th hash   ==> EXPAND:
| size = k (always)       |                                        |                              ADD z to sample_core
|                         |                                        |                              MOVE z_kth_hash from sample_core to sample_xtra
+-------------------------+  <-- k-th hash                         |                              total size ++
|                         |      = min_hash in sample_core         |
|                         |                                        |
| sample_xtra             |                                        |
| size = variable = S - k |                                        |   <-- kth_hash > y &&  ==> REPLACE z_min_hash with z:
|                         |                                        |       y > min_hash           ADD z to sample_xtra
|                         |                                        |                              REMOVE z_min_hash from sample_xtra
|                         |                                        |
+-------------------------+                                        |
             |                   = min_hash in sample_xtra         |
             |                                                     |   <-- y <= min_hash    ==> DISCARD z
             |                                                     |
             v                                                     |
      Low hash values                                              |
                                                                   |
```

## License

This project is licensed under the MIT license, which means that you can do whatever you want with this code, as long as you preserve, in some form, the associated copyright and license notice.
