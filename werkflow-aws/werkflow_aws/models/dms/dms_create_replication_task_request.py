from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr
from .dms_tag import DMSTag


class DMSCreateReplicationTaskRequest(BaseModel):
    ReplicationTaskIdentifier: StrictStr
    SourceEndpointArn: StrictStr
    TargetEndpointArn: StrictStr
    ReplicationInstanceArn: StrictStr
    MigrationType: Literal['full-load', 'cdc', 'full-load-and-cdc']
    TableMappings: StrictStr
    ReplicationTaskSettings: StrictStr | None = None
    CdcStartTime: datetime.datetime | StrictStr | None = None
    CdcStartPosition: StrictStr | None = None
    CdcStopPosition: StrictStr | None = None
    Tags: list[DMSTag] | None = None
    TaskData: StrictStr | None = None
    ResourceIdentifier: StrictStr | None = None
