#!/usr/bin/env python3
"""
Example usage of the Causal Discovery Agent.
"""

import pandas as pd
from src.causal_discovery_agent import CausalDiscoveryAgent

def main():
    # Sample data
    data = pd.DataFrame({
        'Gene1': [1.0, 2.0, 3.0],
        'Gene2': [4.0, 5.0, 6.0],
        'Gene3': [7.0, 8.0, 9.0]
    })
    priors = {}

    config = {
        'reasoning': {},
        'structure_learning': {},
        'experimental_design': {}
    }

    agent = CausalDiscoveryAgent(config)
    experiments = agent.run_discovery_loop(data, priors)
    print(f"Selected experiments: {experiments}")

if __name__ == '__main__':
    main()