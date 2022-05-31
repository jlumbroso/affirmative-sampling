
import math
import typing

import randomhash


def affirmativeSampling(tokens: typing.List[str], k: int):
    
    # initialize the sample
    
    sample_core = set()
    sample_xtra = set()
    sample_freqs = {}
    
    # INITIAL PART
    # ============

    # fill S with the first k distinct elements (and hash values)
    
    idx = 0
    while len(sample_core) < k and idx < len(tokens):
        z = tokens[idx]
        if z not in sample_core:
            sample_core.add(z)
        idx += 1
        
        # update frequency
        sample_freqs[z] = sample_freqs.get(z, 0) + 1
    
    # compute current minimum and kth largest element of the sample
    
    _g = lambda z: (randomhash.hash(z), z)
    min_hash, z_min_hash = min(map(_g, sample_core))  # sample_core here because sample_xtra is empty
    kth_hash, z_kth_hash = min(map(_g, sample_core))

    # MAIN LOOP
    # =========
    
    for z in tokens[idx:]:
        
        # (A) if z in the sample
        if z in sample_core or z in sample_xtra:
            # update frequency
            # (should also update any other stat of z)
            sample_freqs[z] = sample_freqs.get(z, 0) + 1
            continue
        
        # (B) z is not in the sample, so compute y=hash(z)
        
        y = randomhash.hash(z)
 
        # (B.1) if y is smaller than the min hash value in S
        if y < min_hash:
            # DISCARD = ignore the element entirely
            continue

        # (B.2) if y is larger than the k-th largest hash value in S
        # y is a new k-record, needs not to be larger than the largest in the sample!
        elif y > kth_hash:
            # EXPAND = the total size sample grows by one
            # (but sample_core remains at size k)

            # add z to S
            sample_core.add(z)
            sample_freqs[z] = 1

            # move z_kth_hash from core to xtra
            sample_xtra.add(z_kth_hash)
            sample_core.remove(z_kth_hash)

            min_hash, z_min_hash = min(map(_g, sample_xtra))
            kth_hash, z_kth_hash = min(map(_g, sample_core))
            
        # (B.3) otherwise z replaces the element z* with min. hash value
        # sample_xtra must contain z_min_hash otherwise we have a contradiction
        else:
            # REPLACE = the size of the sample does not change but we
            # make sure to keep the largest elements

            # remove the element with min. hash value
            sample_xtra.remove(z_min_hash)
            del sample_freqs[z_min_hash]

            # and replace by the current element z
            sample_xtra.add(z)
            sample_freqs[z] = 1

            # only sample_xtra has changed, no need to update kth_hash
            min_hash, z_min_hash = min(map(_g, sample_xtra))
            
    
    # compute estimators
    recordinality = k*(1 + 1/k)**(len(sample_freqs)-k+1)
    af_kmv = (len(sample_freqs)-1)/(1-randomhash.int_to_real(min_hash))
    expected_sample_size = k*math.log(n/k) + k
    
    return {
        "cardinality": {
            "recordinality": recordinality,
            "af-kmv": af_kmv,
        },
        "expectedSampleSize": expected_sample_size,
        "sampleSize": len(sample_freqs),
        "sample": sample_freqs
    }