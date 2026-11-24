from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jql_function_precomputation_bean import JqlFunctionPrecomputationBean


class JqlFunctionPrecomputationGetByIdResponse(BaseModel):
    notFoundPrecomputationIDs: list[StrictStr] | None = None
    precomputations: list[JqlFunctionPrecomputationBean] | None = None
