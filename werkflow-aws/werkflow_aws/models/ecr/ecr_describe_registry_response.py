from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_replication_configuration import ECRReplicationConfiguration


class ECRDescribeRegistryResponse(BaseModel):
    registryId: StrictStr | None = None
    replicationConfiguration: ECRReplicationConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
