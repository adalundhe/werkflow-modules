from __future__ import annotations
from typing import TypeAlias
from .issue_context_variable import IssueContextVariable
from .json_context_variable import JsonContextVariable
from .user_context_variable import UserContextVariable

CustomContextVariable: TypeAlias = UserContextVariable | IssueContextVariable | JsonContextVariable
