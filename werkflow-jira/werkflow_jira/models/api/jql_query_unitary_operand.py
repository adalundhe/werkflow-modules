from __future__ import annotations
from typing import TypeAlias
from .function_operand import FunctionOperand
from .keyword_operand import KeywordOperand
from .value_operand import ValueOperand

JqlQueryUnitaryOperand: TypeAlias = ValueOperand | FunctionOperand | KeywordOperand
