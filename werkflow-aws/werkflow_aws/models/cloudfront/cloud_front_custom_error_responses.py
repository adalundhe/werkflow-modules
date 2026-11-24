from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_front_custom_error_response import CloudFrontCustomErrorResponse


class CloudFrontCustomErrorResponses(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[CloudFrontCustomErrorResponse] | None = None
