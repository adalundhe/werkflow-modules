from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .cloud_front_kg_key_pair_ids import CloudFrontKGKeyPairIds


class CloudFrontActiveTrustedKeyGroups(BaseModel):
    Enabled: StrictBool | None = None
    Quantity: StrictInt | None = None
    Items: list[CloudFrontKGKeyPairIds] | None = None
