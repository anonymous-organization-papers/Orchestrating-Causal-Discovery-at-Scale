"""
Main Agentic Framework for Causal Discovery at Scale.

Integrates reasoning, differentiable structure learning, and active experimentation.
"""

from .reasoning import CGoT
from .structure_learning import DifferentiableStructureLearner
from .experimental_design import BayesianOptimalExperimentalDesign


class CausalDiscoveryAgent:
    def __init__(self, config):
        self.config = config
        self.reasoning = CGoT(config.get('reasoning', {}))
        self.structure_learner = DifferentiableStructureLearner(config.get('structure_learning', {}))
        self.experimental_design = BayesianOptimalExperimentalDesign(config.get('experimental_design', {}))

    def run_discovery_loop(self, data, priors):
        """
        Main discovery loop.
        """
        # Hypotheses from reasoning
        hypotheses = self.reasoning.generate_hypotheses(data, priors)
        
        # Learn structure
        structure = self.structure_learner.learn(hypotheses, data)
        
        # Select experiments
        experiments = self.experimental_design.select_experiments(structure, data)
        
        return experiments