# Orchestrating Causal Discovery at Scale

An agentic framework integrating reasoning, differentiable structure learning, and active experimentation.

## Overview

This project implements the framework described in the paper "Orchestrating Causal Discovery at Scale: An Agentic Framework Integrating Reasoning, Differentiable Structure Learning, and Active Experimentation".

The framework consists of three main components:

1. **Causal Graph-of-Thoughts (C-GoT)**: Structured reasoning state for hypotheses, evidence, and decisions.
2. **Differentiable Structure Learning**: Scalable causal structure learning under constraints.
3. **Bayesian Optimal Experimental Design (BOED)**: Selection of informative interventions.

## Installation

```bash
pip install -r requirements.txt
```

## Project Structure

```
src/causal_discovery_agent/
├── __init__.py
├── agent.py                 # Main agent class
├── reasoning/
│   ├── __init__.py
│   └── cgot.py              # C-GoT implementation
├── structure_learning/
│   ├── __init__.py
│   └── learner.py           # Differentiable structure learner
└── experimental_design/
    ├── __init__.py
    └── boed.py              # BOED implementation
tests/
├── test_agent.py
requirements.txt
README.md
example.py
```

## Usage

```python
from causal_discovery_agent import CausalDiscoveryAgent

config = {
    'reasoning': {},
    'structure_learning': {},
    'experimental_design': {}
}

agent = CausalDiscoveryAgent(config)
experiments = agent.run_discovery_loop(data, priors)
```

See `example.py` for a complete example.

## Testing

```bash
python -m unittest tests/
```