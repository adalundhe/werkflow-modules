from __future__ import annotations
from typing import Literal


SageMakerEvaluationType = Literal[
    'LLMAJEvaluation',
    'CustomScorerEvaluation',
    'BenchmarkEvaluation',
]
