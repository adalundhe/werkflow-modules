from __future__ import annotations
from pydantic import BaseModel
from .jql_function_precomputation_update_bean import JqlFunctionPrecomputationUpdateBean


class JqlFunctionPrecomputationUpdateRequestBean(BaseModel):
    values: list[JqlFunctionPrecomputationUpdateBean] | None = None
