"""Implement tests."""
import numpy as np
import unittest
from hypothesis import strategies as strats
from hypothesis import given

from sparse_deconvolution_1D import paper_env


@strats.composite
def env(draw):
    seed = draw(strats.integers(0, 2**32 - 1))
    np.random.seed(seed)
    return paper_env(5)


class TestSparseDeconvolution(unittest.TestCase):
    """Test the sparse deconvolution example."""

    @given(env=env())
    def test_w(self, env):
        assert env.w.shape == (5,)
        abs_w = np.absolute(env.w)
        assert ((0.5 <= abs_w) & (abs_w <= 1.5)).all()

    @given(env=env())
    def test_p(self, env):
        assert env.p.shape == (5,)
        assert ((0 <= env.p) & (env.p <= 1)).all()

    @given(env=env())
    def test_y(self, env):
        env.y(np.linspace(0, 1, 10))

    @given(env=env())
    def test_R(self, env):
        r1 = env.R(np.ones(10))
        r2 = env.R(np.ones((1, 10)))
        r3 = env.R(np.ones((2, 10)))

        assert r1.shape == (1, )
        assert r2.shape == (1,)
        assert r3.shape == (2,)