from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .msk_kafka_cluster_description import MSKKafkaClusterDescription
from .msk_log_delivery import MSKLogDelivery
from .msk_replication_info_description import MSKReplicationInfoDescription
from .msk_replication_state_info import MSKReplicationStateInfo


class MSKDescribeReplicatorResponse(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    CurrentVersion: StrictStr | None = None
    IsReplicatorReference: StrictBool | None = None
    KafkaClusters: list[MSKKafkaClusterDescription] | None = None
    ReplicationInfoList: list[MSKReplicationInfoDescription] | None = None
    ReplicatorArn: StrictStr | None = None
    ReplicatorDescription: StrictStr | None = None
    ReplicatorName: StrictStr | None = None
    ReplicatorResourceArn: StrictStr | None = None
    ReplicatorState: StrictStr | None = None
    ServiceExecutionRoleArn: StrictStr | None = None
    StateInfo: MSKReplicationStateInfo | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    LogDelivery: MSKLogDelivery | None = None
    ResponseMetadata: dict[str, Any] | None = None
