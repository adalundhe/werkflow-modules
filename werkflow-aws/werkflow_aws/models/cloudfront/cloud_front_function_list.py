from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_function_summary import CloudFrontFunctionSummary


class CloudFrontFunctionList(BaseModel):
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontFunctionSummary] | None = None
