from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_public_key import CloudTrailPublicKey


class CloudTrailListPublicKeysResponse(BaseModel):
    PublicKeyList: list[CloudTrailPublicKey] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
