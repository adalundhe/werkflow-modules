from __future__ import annotations
from typing import TypeAlias
from .workflow_compound_condition import WorkflowCompoundCondition
from .workflow_simple_condition import WorkflowSimpleCondition

WorkflowCondition: TypeAlias = WorkflowSimpleCondition | WorkflowCompoundCondition
