"""
Bayesian Optimal Experimental Design for causal discovery.
"""

import numpy as np


class BayesianOptimalExperimentalDesign:
    def __init__(self, config):
        self.config = config

    def select_experiments(self, structure, data):
        """
        Select interventions that maximize information gain.
        """
        # Placeholder: random selection
        n_vars = structure.shape[0]
        n_select = min(5, n_vars)
        experiments = np.random.choice(n_vars, size=n_select, replace=False)
        return list(experiments)