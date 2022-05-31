
import randomhash

def affirmativeSampling(k, tokens):
    
    min_hash = None
    
    # fill S with the first k distinct elements (and hash values)
    
    sample_core = set()
    sample_xtra = set()
    sample_freqs = {}
    idx = 0
    while len(sample_core) < k and idx < len(tokens):
        z = tokens[idx]
        if z not in sample_core:
            sample_core.add(z)
        idx += 1
        
        # update frequency
        sample_freqs[z] = sample_freqs.get(z, 0) + 1
    
    # compute current minimum
    
    _g = lambda z: (randomhash.hash(z), z)
    min_hash, z_min_hash = min(map(_g, sample_core))
    max_hash, z_max_hash = max(map(_g, sample_core))
    
    # main loop
    
    for z in tokens[idx:]:
        
        # if z in the sample
        if z in sample_core or z in sample_xtra:
            # updating frequency
            # (should also update any other stat of z)
            sample_freqs[z] = sample_freqs.get(z, 0) + 1
            continue
        
        # z is not in the sample, so compute y=hash(z)
        
        y = randomhash.hash(z)
        
        #   sample -----------\
        #                     |
        #          min_hash   |   k-th largest hash value
        #             |       |            |
        #             v       v            v
        # 0 --------- [[<elem_1>, ..., <elem_k>]] --------- 1
        #   DISCARD  |         REPLACE          | EXPAND
        #
        
        # if y is smaller than the min hash value in S
        if y < min_hash:
            # DISCARD(/IGNORE)
            continue
        
        # if y is larger than the k-th largest hash value in S
        # (if y is larger than any hash value in the sample)
        elif y > max_hash:
            # EXPAND
            sample_xtra.add(z)
        
        # otherwise z replaces the element z* with min. hash value
        else:
            # REPLACE
            # remove z*
            sample_core.remove(z_min_hash)
            sample_freqs.remove(z_min_hash)
            
            # add z
            sample_core.add(z)
            sample_freqs[z] = 1
            
            # update min/max
            min_hash, z_min_hash = min(map(_g, sample_core))
            max_hash, z_max_hash = max(map(_g, sample_core))
            
    
    return sample_freqs, len(sample_core), len(sample_xtra)