from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_public_key_summary import CloudFrontPublicKeySummary


class CloudFrontPublicKeyList(BaseModel):
    NextMarker: StrictStr | None = None
    MaxItems: StrictInt | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontPublicKeySummary] | None = None
