from __future__ import annotations
from typing import TypeAlias
from .function_operand import FunctionOperand
from .keyword_operand import KeywordOperand
from .list_operand import ListOperand
from .value_operand import ValueOperand

JqlQueryClauseOperand: TypeAlias = ListOperand | ValueOperand | FunctionOperand | KeywordOperand
