from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_replication_configuration import ECRReplicationConfiguration


class ECRPutReplicationConfigurationResponse(BaseModel):
    replicationConfiguration: ECRReplicationConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
