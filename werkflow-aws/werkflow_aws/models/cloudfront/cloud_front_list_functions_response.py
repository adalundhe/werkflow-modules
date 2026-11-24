from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_function_list import CloudFrontFunctionList


class CloudFrontListFunctionsResponse(BaseModel):
    FunctionList: CloudFrontFunctionList | None = None
    ResponseMetadata: dict[str, Any] | None = None
