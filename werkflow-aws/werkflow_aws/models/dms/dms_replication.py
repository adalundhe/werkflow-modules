from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .dms_premigration_assessment_status import DMSPremigrationAssessmentStatus
from .dms_provision_data import DMSProvisionData
from .dms_replication_stats import DMSReplicationStats


class DMSReplication(BaseModel):
    ReplicationConfigIdentifier: StrictStr | None = None
    ReplicationConfigArn: StrictStr | None = None
    SourceEndpointArn: StrictStr | None = None
    TargetEndpointArn: StrictStr | None = None
    ReplicationType: StrictStr | None = None
    Status: StrictStr | None = None
    ProvisionData: DMSProvisionData | None = None
    PremigrationAssessmentStatuses: list[DMSPremigrationAssessmentStatus] | None = None
    StopReason: StrictStr | None = None
    FailureMessages: list[StrictStr] | None = None
    ReplicationStats: DMSReplicationStats | None = None
    StartReplicationType: StrictStr | None = None
    CdcStartTime: datetime.datetime | StrictStr | None = None
    CdcStartPosition: StrictStr | None = None
    CdcStopPosition: StrictStr | None = None
    RecoveryCheckpoint: StrictStr | None = None
    ReplicationCreateTime: datetime.datetime | StrictStr | None = None
    ReplicationUpdateTime: datetime.datetime | StrictStr | None = None
    ReplicationLastStopTime: datetime.datetime | StrictStr | None = None
    ReplicationDeprovisionTime: datetime.datetime | StrictStr | None = None
    IsReadOnly: StrictBool | None = None
