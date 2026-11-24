from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .dms_compute_config import DMSComputeConfig


class DMSReplicationConfig(BaseModel):
    ReplicationConfigIdentifier: StrictStr | None = None
    ReplicationConfigArn: StrictStr | None = None
    SourceEndpointArn: StrictStr | None = None
    TargetEndpointArn: StrictStr | None = None
    ReplicationType: StrictStr | None = None
    ComputeConfig: DMSComputeConfig | None = None
    ReplicationSettings: StrictStr | None = None
    SupplementalSettings: StrictStr | None = None
    TableMappings: StrictStr | None = None
    ReplicationConfigCreateTime: datetime.datetime | StrictStr | None = None
    ReplicationConfigUpdateTime: datetime.datetime | StrictStr | None = None
    IsReadOnly: StrictBool | None = None
