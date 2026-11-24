from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .cloud_front_origin import CloudFrontOrigin


class CloudFrontOrigins(BaseModel):
    Quantity: StrictInt | None = None
    Items: list[CloudFrontOrigin] | None = None
