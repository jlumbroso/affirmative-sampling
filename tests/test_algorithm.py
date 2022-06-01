
import pytest

import affirmative_sampling.algorithm

_ONE_TOKEN = ["a"]
_TWO_TOKENS = ["a", "b"]
_SEVERAL_TOKENS = ["a", "b", "c", "d", "e"]
_SOME_K = 1

def test_call_affirmative_sampling_one_token_k_to_size():
    affirmative_sampling.algorithm.affirmative_sampling(tokens=_ONE_TOKEN, k=len(_ONE_TOKEN))

def test_call_affirmative_sampling_several_unique_token_k_to_size():
    affirmative_sampling.algorithm.affirmative_sampling(tokens=_SEVERAL_TOKENS, k=len(_SEVERAL_TOKENS))

def test_call_affirmative_sampling_several_unique_token_k_smaller():
    affirmative_sampling.algorithm.affirmative_sampling(
        tokens=_SEVERAL_TOKENS,
        k=min(_SOME_K, len(_SEVERAL_TOKENS))
    )

@pytest.mark.repeat(10)
def test_call_affirmative_sampling_several_repeated_token_k_smaller():
    affirmative_sampling.algorithm.affirmative_sampling(
        tokens=_SEVERAL_TOKENS * 2,
        k=min(_SOME_K, len(_SEVERAL_TOKENS))
    )