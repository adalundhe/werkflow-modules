from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class GlueGetUserDefinedFunctionsRequest(BaseModel):
    Pattern: StrictStr
    CatalogId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    FunctionType: Literal['REGULAR_FUNCTION', 'AGGREGATE_FUNCTION', 'STORED_PROCEDURE'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
