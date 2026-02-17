"""
Tests for Causal Discovery Agent.
"""

import unittest
import pandas as pd
import torch
from src.causal_discovery_agent import CausalDiscoveryAgent


class TestAgent(unittest.TestCase):
    def setUp(self):
        self.config = {}
        self.agent = CausalDiscoveryAgent(self.config)

    def test_run_loop(self):
        # Mock data
        data = pd.DataFrame({'A': [1,2,3], 'B': [4,5,6], 'C': [7,8,9]})
        priors = {}
        experiments = self.agent.run_discovery_loop(data, priors)
        self.assertIsInstance(experiments, list)


if __name__ == '__main__':
    unittest.main()