from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsDmsReplicationTaskDetails(BaseModel):
    CdcStartPosition: StrictStr | None = None
    CdcStartTime: StrictStr | None = None
    CdcStopPosition: StrictStr | None = None
    MigrationType: StrictStr | None = None
    Id: StrictStr | None = None
    ResourceIdentifier: StrictStr | None = None
    ReplicationInstanceArn: StrictStr | None = None
    ReplicationTaskIdentifier: StrictStr | None = None
    ReplicationTaskSettings: StrictStr | None = None
    SourceEndpointArn: StrictStr | None = None
    TableMappings: StrictStr | None = None
    TargetEndpointArn: StrictStr | None = None
    TaskData: StrictStr | None = None
