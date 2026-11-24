from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .dms_replication_task_stats import DMSReplicationTaskStats


class DMSReplicationTask(BaseModel):
    ReplicationTaskIdentifier: StrictStr | None = None
    SourceEndpointArn: StrictStr | None = None
    TargetEndpointArn: StrictStr | None = None
    ReplicationInstanceArn: StrictStr | None = None
    MigrationType: StrictStr | None = None
    TableMappings: StrictStr | None = None
    ReplicationTaskSettings: StrictStr | None = None
    Status: StrictStr | None = None
    LastFailureMessage: StrictStr | None = None
    StopReason: StrictStr | None = None
    ReplicationTaskCreationDate: datetime.datetime | StrictStr | None = None
    ReplicationTaskStartDate: datetime.datetime | StrictStr | None = None
    CdcStartPosition: StrictStr | None = None
    CdcStopPosition: StrictStr | None = None
    RecoveryCheckpoint: StrictStr | None = None
    ReplicationTaskArn: StrictStr | None = None
    ReplicationTaskStats: DMSReplicationTaskStats | None = None
    TaskData: StrictStr | None = None
    TargetReplicationInstanceArn: StrictStr | None = None
