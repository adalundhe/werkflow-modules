from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_kafka_cluster import MSKKafkaCluster
from .msk_log_delivery import MSKLogDelivery
from .msk_replication_info import MSKReplicationInfo


class MSKCreateReplicatorRequest(BaseModel):
    KafkaClusters: list[MSKKafkaCluster]
    ReplicationInfoList: list[MSKReplicationInfo]
    ReplicatorName: StrictStr
    ServiceExecutionRoleArn: StrictStr
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    LogDelivery: MSKLogDelivery | None = None
