from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .dms_compute_config import DMSComputeConfig


class DMSModifyReplicationConfigRequest(BaseModel):
    ReplicationConfigArn: StrictStr
    ReplicationConfigIdentifier: StrictStr | None = None
    ReplicationType: Literal['full-load', 'cdc', 'full-load-and-cdc'] | None = None
    TableMappings: StrictStr | None = None
    ReplicationSettings: StrictStr | None = None
    SupplementalSettings: StrictStr | None = None
    ComputeConfig: DMSComputeConfig | None = None
    SourceEndpointArn: StrictStr | None = None
    TargetEndpointArn: StrictStr | None = None
