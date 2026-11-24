from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .cloud_front_signer import CloudFrontSigner


class CloudFrontActiveTrustedSigners(BaseModel):
    Enabled: StrictBool | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontSigner] | None = None
