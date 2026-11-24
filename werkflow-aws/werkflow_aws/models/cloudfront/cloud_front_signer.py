from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_key_pair_ids import CloudFrontKeyPairIds


class CloudFrontSigner(BaseModel):
    AwsAccountNumber: StrictStr | None = None
    KeyPairIds: CloudFrontKeyPairIds | None = None
