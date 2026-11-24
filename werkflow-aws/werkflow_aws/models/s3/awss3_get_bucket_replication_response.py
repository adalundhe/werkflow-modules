from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_replication_configuration import AWSS3ReplicationConfiguration


class AWSS3GetBucketReplicationResponse(BaseModel):
    ReplicationConfiguration: AWSS3ReplicationConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
