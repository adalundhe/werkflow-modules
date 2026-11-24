from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_user_defined_function import GlueUserDefinedFunction


class GlueGetUserDefinedFunctionResponse(BaseModel):
    UserDefinedFunction: GlueUserDefinedFunction | None = None
    ResponseMetadata: dict[str, Any] | None = None
