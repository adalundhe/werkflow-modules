from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .jql_function_precomputation_bean import JqlFunctionPrecomputationBean


class PageBean2JqlFunctionPrecomputationBean(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[JqlFunctionPrecomputationBean] | None = None
