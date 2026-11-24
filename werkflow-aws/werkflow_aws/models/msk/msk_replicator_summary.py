from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .msk_kafka_cluster_summary import MSKKafkaClusterSummary
from .msk_replication_info_summary import MSKReplicationInfoSummary


class MSKReplicatorSummary(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    CurrentVersion: StrictStr | None = None
    IsReplicatorReference: StrictBool | None = None
    KafkaClustersSummary: list[MSKKafkaClusterSummary] | None = None
    ReplicationInfoSummaryList: list[MSKReplicationInfoSummary] | None = None
    ReplicatorArn: StrictStr | None = None
    ReplicatorName: StrictStr | None = None
    ReplicatorResourceArn: StrictStr | None = None
    ReplicatorState: StrictStr | None = None
