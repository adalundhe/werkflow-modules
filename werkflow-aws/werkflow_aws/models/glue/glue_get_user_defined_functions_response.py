from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_user_defined_function import GlueUserDefinedFunction


class GlueGetUserDefinedFunctionsResponse(BaseModel):
    UserDefinedFunctions: list[GlueUserDefinedFunction] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
