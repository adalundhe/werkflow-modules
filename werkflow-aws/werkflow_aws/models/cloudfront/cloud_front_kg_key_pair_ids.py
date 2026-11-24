from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_key_pair_ids import CloudFrontKeyPairIds


class CloudFrontKGKeyPairIds(BaseModel):
    KeyGroupId: StrictStr | None = None
    KeyPairIds: CloudFrontKeyPairIds | None = None
