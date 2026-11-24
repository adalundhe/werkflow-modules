from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_front_origin_custom_header import CloudFrontOriginCustomHeader


class CloudFrontCustomHeaders(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[CloudFrontOriginCustomHeader] | None = None
