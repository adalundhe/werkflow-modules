from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .efs_replication_configuration_description import EFSReplicationConfigurationDescription


class EFSDescribeReplicationConfigurationsResponse(BaseModel):
    Replications: list[EFSReplicationConfigurationDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
