from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .dms_compute_config import DMSComputeConfig
from .dms_tag import DMSTag


class DMSCreateReplicationConfigRequest(BaseModel):
    ReplicationConfigIdentifier: StrictStr
    SourceEndpointArn: StrictStr
    TargetEndpointArn: StrictStr
    ComputeConfig: DMSComputeConfig
    ReplicationType: Literal['full-load', 'cdc', 'full-load-and-cdc']
    TableMappings: StrictStr
    ReplicationSettings: StrictStr | None = None
    SupplementalSettings: StrictStr | None = None
    ResourceIdentifier: StrictStr | None = None
    Tags: list[DMSTag] | None = None
