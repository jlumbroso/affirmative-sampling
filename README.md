# Affirmative Sampling: Reference Implementation

[![DOI](https://zenodo.org/badge/474830155.svg)](https://zenodo.org/badge/latestdoi/474830155)
[![pytest](https://github.com/jlumbroso/affirmative-sampling/actions/workflows/continuous-integration.yaml/badge.svg)](https://github.com/jlumbroso/affirmative-sampling/actions/workflows/continuous-integration.yaml)
[![codecov](https://codecov.io/gh/jlumbroso/affirmative-sampling/branch/main/graph/badge.svg?token=4S8TD999YC)](https://codecov.io/gh/jlumbroso/affirmative-sampling)

This repository contains a reference implementation, in Python, of the _Affirmative Sampling_ algorithm by Jérémie Lumbroso and Conrado Martínez (2022), as well as the original paper, accepted at the Analysis of Algorithms 2022 edition in Philadelphia.

**Table of contents:**

- [Abstract](#abstract)
- [Installation](#installation)
- [Historical Context](#historical-context)
- [Example](#example)
- [Intuition of How the Random Sample Grows](#intuition-of-how-the-random-sample-grows)
- [License](#license)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>ToC generated with markdown-toc</a></i></small>

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

## Example

You can look and run an example. Assuming you have `pipenv`:

```shell
$ pipenv run python example.py
```

or otherwise assuming your current Python environment has the package `affirmative_sampling` installed:

```shell
$ python example.py
```

The output will be something along the following lines (exact value will change as the seed depends on the computer's clock):

```
=====================================================
'Affirmative Sampling' by J. Lumbroso and C. Martínez
=====================================================

   Examples use Moby Dick (from the Gutenberg Project)
   N=215436, n=19962, k=100, k*ln(n/k)=629.641555925844

EXAMPLE 1: Number of tokens without 'e'
====================================
- Exact count: 6839
- Estimated count: 7398.94
  - Error: 8.19%

- Size of sample: 648
   - Expected size of sample: 629.64
   - Tokens in sample without 'e': 242
   - Proportion of tokens in sample without 'e': 37.35%


EXAMPLE 2: Number of mice (freq. less or equal to 5)
====================================================
- Exact count: 16450
- Estimated count: 16999.21
  - Error: 3.34%

- Size of sample: 648
   - Expected size of sample: 629.64
   - Tokens in sample without 'e': 556
   - Proportion of tokens in sample without 'e': 85.8%

SAMPLE
======
 1780 but
  427 would
  315 do
  165 water
  103 sight
   86 give
   68 name
   61 together
   54 entire
   43 straight
   37 famous
   33 idea
   31 mariners
   29 person
   29 stands
   27 wooden
   26 circumstance
   26 cutting
   26 otherwise
   25 souls
   22 aboard
   22 owing
   20 ah
   19 concluded
   19 deeper
   19 leaves
   19 ordinary
   18 anchor
   18 presently
   17 foolish
   17 previously
   17 weight
   16 fate
   15 fit
   15 flag
   15 grass
   15 shake
   14 intent
   14 rock
   13 bunger
   13 cool
   13 eager
   13 glancing
   13 slightly
   13 token
   13 trademark
   13 visit
   12 america
   12 smells
   12 solemn
   12 street
   12 touched
   11 ashes
   11 carefully
   11 carpenters
   11 dish
   11 downwards
   11 sounding
   11 stream
   10 event
   10 inferior
   10 lift
   10 perch
    9 cask
    9 change
    9 driving
    9 everlasting
    8 crushed
    8 currents
    8 damp
    8 leviathanic
    8 mayhew
    8 monkey
    8 ought
    8 published
    8 shooting
    8 strove
    7 cracked
    7 destined
    7 knocking
    7 lookout
    6 arch
    6 bury
    6 cheek
    6 comfort
    6 decent
    6 longitude
    6 probable
    6 purple
    6 subjects
    6 symptoms
    6 value
    5 depend
    5 dip
    5 disordered
    5 faded
    5 fasten
    5 france
    5 guard
    5 humming
    5 invited
    5 navy
    5 paradise
    5 pen
    5 riveted
    5 rude
    5 specimen
    5 sufficient
    5 wait
    4 anchored
    4 arsacidean
    4 assert
    4 beast
    4 beaver
    4 blubberroom
    4 boatknife
    4 cease
    4 damages
    4 distinguish
    4 fidelity
    4 follows
    4 gills
    4 hearses
    4 moves
    4 music
    4 ninety
    4 offers
    4 paintings
    4 razor
    4 respectfully
    4 scorching
    4 sets
    4 spaniards
    4 standers
    4 stroll
    4 supposition
    4 tufted
    4 unrecorded
    3 asiatic
    3 behooves
    3 brilliancy
    3 capacity
    3 capricious
    3 cares
    3 characteristics
    3 charley
    3 churned
    3 closet
    3 cuts
    3 describe
    3 disposition
    3 dodge
    3 entity
    3 epidemic
    3 eternities
    3 extinct
    3 fancies
    3 figured
    3 fleetness
    3 flooded
    3 flurry
    3 grizzled
    3 halls
    3 hip
    3 inconsiderable
    3 inmates
    3 inseparable
    3 mending
    3 mule
    3 pouring
    3 pregnant
    3 providence
    3 quoted
    3 rags
    3 romish
    3 route
    3 shun
    3 smoky
    3 socks
    3 spots
    3 stained
    3 stolen
    3 substantiated
    3 suspect
    3 tarpaulins
    3 tashtegos
    3 thrusts
    3 ticklish
    3 tows
    3 tragedy
    3 treat
    3 typhoons
    3 unabated
    3 user
    3 weighty
    3 westward
    3 whittling
    3 wraps
    2 accessible
    2 admitting
    2 admonished
    2 aglow
    2 agonized
    2 alluding
    2 attain
    2 avenues
    2 awed
    2 backwoodsman
    2 barely
    2 belshazzars
    2 bout
    2 brag
    2 bravest
    2 bumps
    2 burkes
    2 ceases
    2 chancelike
    2 chasefirst
    2 complement
    2 confidently
    2 constitution
    2 cows
    2 cringing
    2 decanting
    2 digest
    2 dilapidated
    2 distinctive
    2 dusting
    2 egotistical
    2 enlivened
    2 ensue
    2 entrances
    2 error
    2 essentially
    2 exertion
    2 expiring
    2 faraway
    2 fearlessly
    2 fishe
    2 fishspears
    2 girdling
    2 glide
    2 grammar
    2 halloo
    2 hilariously
    2 housekeeping
    2 hover
    2 hudson
    2 imputation
    2 injured
    2 junks
    2 keyhole
    2 manofwar
    2 masterless
    2 meridian
    2 misanthropic
    2 navel
    2 newspaper
    2 obligations
    2 opulent
    2 oughts
    2 outlast
    2 outwardbound
    2 overseeing
    2 paramount
    2 penetrating
    2 performed
    2 permitting
    2 pumping
    2 quaint
    2 quilt
    2 rabelais
    2 reappeared
    2 regulating
    2 ripple
    2 ruinous
    2 sadder
    2 sagittarius
    2 saltsea
    2 scandinavian
    2 scratches
    2 serves
    2 shunned
    2 snows
    2 squeezed
    2 stiffest
    2 sympathies
    2 tarpaulin
    2 temperature
    2 texas
    2 toilings
    2 tweezers
    2 underneath
    2 unthinkingly
    2 unwarrantably
    2 ushered
    2 vagabond
    2 whalehunters
    2 woodlands
    1 abstemious
    1 accomplishment
    1 acquiesce
    1 admirer
    1 adoring
    1 affghanistan
    1 afterhes
    1 ahabshudder
    1 airfreighted
    1 alpine
    1 amosti
    1 ancestress
    1 andromedaindeed
    1 animosity
    1 annually
    1 antecedent
    1 aroostook
    1 arter
    1 asa
    1 atom
    1 attarofrose
    1 backof
    1 ballena
    1 bamboozingly
    1 bamboozle
    1 battled
    1 bays
    1 bedclothes
    1 beehive
    1 bellbuttons
    1 bestreaked
    1 billiardball
    1 billiardballs
    1 boatsmark
    1 boatswain
    1 brandingiron
    1 breedeth
    1 brutal
    1 brutes
    1 bungle
    1 burlybrowed
    1 cajoling
    1 cambrics
    1 centipede
    1 channel
    1 characteristically
    1 chickens
    1 circumambient
    1 clapt
    1 claw
    1 claws
    1 cloudscud
    1 colorless
    1 commentator
    1 confidentially
    1 congeniality
    1 connexions
    1 consolatory
    1 constrain
    1 contiguity
    1 controllable
    1 costermongers
    1 couldin
    1 counteracted
    1 counterbalanced
    1 counters
    1 courtesymay
    1 coverlid
    1 creware
    1 crookedness
    1 crownjewels
    1 czarship
    1 dallied
    1 deaden
    1 decisionone
    1 defiles
    1 delightwho
    1 demonism
    1 departing
    1 detects
    1 digester
    1 dines
    1 disbands
    1 discipline
    1 dissolve
    1 domineered
    1 donned
    1 donthe
    1 doubleshuffle
    1 doubling
    1 doughnuts
    1 dubiouslooking
    1 dugongs
    1 dumbest
    1 dwarfed
    1 earththat
    1 eavetroughs
    1 ego
    1 ellery
    1 elucidating
    1 emoluments
    1 englishknowing
    1 engraven
    1 enthusiasmbut
    1 errorabounding
    1 eventuated
    1 exaggerate
    1 exegetists
    1 exploring
    1 expressly
    1 exultation
    1 factories
    1 feasting
    1 featuring
    1 ferdinando
    1 fiercefanged
    1 fissures
    1 fitsthats
    1 flavorish
    1 froissart
    1 funereally
    1 furs
    1 garterknights
    1 ghastliness
    1 glimmering
    1 gloss
    1 glows
    1 godomnipresent
    1 grease
    1 greenly
    1 grog
    1 groupings
    1 guido
    1 halfbelieved
    1 hangdog
    1 hayseed
    1 headladen
    1 heraldic
    1 hitching
    1 hoarfrost
    1 honing
    1 hopefulness
    1 horned
    1 hussars
    1 ifand
    1 ignore
    1 ignoring
    1 ills
    1 illumination
    1 imitated
    1 import
    1 incidents
    1 indianfile
    1 inflated
    1 instigation
    1 intangible
    1 intercedings
    1 interflow
    1 inventing
    1 inventors
    1 irresolution
    1 ithow
    1 ixion
    1 jobcoming
    1 jollynot
    1 jugglers
    1 lackaday
    1 lacks
    1 ladthe
    1 lakeevinced
    1 laureate
    1 legmaker
    1 lend
    1 leopardsthe
    1 leviathanism
    1 lifeas
    1 lighten
    1 lighthouse
    1 lordvishnoo
    1 lovings
    1 maintruckha
    1 maltreated
    1 manufacturer
    1 marquee
    1 meatmarket
    1 miasmas
    1 midnighthow
    1 migrating
    1 milkiness
    1 misfortune
    1 mixing
    1 mock
    1 moons
    1 mossy
    1 mutinying
    1 mystically
    1 namelessly
    1 nantuckois
    1 napoleons
    1 naythe
    1 negligence
    1 neighborsthe
    1 netted
    1 nondescripts
    1 offwe
    1 oftenest
    1 ohwhew
    1 oilpainting
    1 onsets
    1 overbalance
    1 overdoing
    1 palpableness
    1 panicstricken
    1 parenthesize
    1 particoloured
    1 pascal
    1 pauselessly
    1 pave
    1 peddlin
    1 pedestal
    1 perturbation
    1 pester
    1 philopater
    1 plaintively
    1 platos
    1 poker
    1 prescribed
    1 princess
    1 proas
    1 propulsion
    1 prtorians
    1 queerqueer
    1 quitthe
    1 quivered
    1 rads
    1 rarities
    1 readable
    1 reasona
    1 rechristened
    1 regardless
    1 reglar
    1 repent
    1 reverenced
    1 reveriestallied
    1 rightdown
    1 rioting
    1 rob
    1 rosesome
    1 rustling
    1 saidtherefore
    1 sawlightning
    1 sayshands
    1 scoot
    1 scornfully
    1 scuffling
    1 seafowl
    1 seamless
    1 seasalt
    1 seconds
    1 sedentary
    1 seducing
    1 selfcollectedness
    1 sheathed
    1 shindy
    1 shipwhich
    1 shirrbut
    1 shortwarpthe
    1 shoutedsail
    1 sideladder
    1 silverso
    1 singlesheaved
    1 sirin
    1 slanderous
    1 soars
    1 sodom
    1 songster
    1 sphynxs
    1 spill
    1 spoiling
    1 spurzheim
    1 starbuckbut
    1 staterooms
    1 stingy
    1 stoopingly
    1 sunburnt
    1 superseded
    1 surcoat
    1 surpassingly
    1 surveying
    1 syren
    1 tenement
    1 terribleness
    1 theni
    1 therethe
    1 thingbe
    1 thingnamely
    1 thingsoak
    1 thinkbut
    1 thisgreen
    1 thisthe
    1 thunderclotted
    1 ticdollyrow
    1 tick
    1 ticking
    1 tie
    1 timberhead
    1 tipping
    1 topple
    1 tracingsout
    1 traditional
    1 trans
    1 treachery
    1 treasuries
    1 trivial
    1 trumpblister
    1 tunnels
    1 unblinkingly
    1 unchallenged
    1 undecided
    1 undefiled
    1 underground
    1 unequal
    1 unfavourable
    1 unfractioned
    1 unmisgiving
    1 unsay
    1 unthought
    1 usei
    1 vanquished
    1 victory
    1 virgo
    1 volunteered
    1 wading
    1 wales
    1 wan
    1 wary
    1 waythats
    1 weathersheet
    1 weaverpauseone
    1 wept
    1 wethough
    1 whalethis
    1 whalewise
    1 winces
    1 workmen
    1 worm
    1 wornout
    1 worseat
    1 zip
```

## Intuition of How the Random Sample Grows

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
