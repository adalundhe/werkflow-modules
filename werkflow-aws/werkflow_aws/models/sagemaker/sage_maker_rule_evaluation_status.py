from __future__ import annotations
from typing import Literal


SageMakerRuleEvaluationStatus = Literal[
    'InProgress',
    'NoIssuesFound',
    'IssuesFound',
    'Error',
    'Stopping',
    'Stopped',
]
