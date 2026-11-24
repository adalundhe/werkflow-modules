from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kms_key_metadata import KMSKeyMetadata
from .kms_tag import KMSTag


class KMSReplicateKeyResponse(BaseModel):
    ReplicaKeyMetadata: KMSKeyMetadata | None = None
    ReplicaPolicy: StrictStr | None = None
    ReplicaTags: list[KMSTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
