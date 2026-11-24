from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_consumer_group_replication_update import MSKConsumerGroupReplicationUpdate
from .msk_log_delivery import MSKLogDelivery
from .msk_topic_replication_update import MSKTopicReplicationUpdate


class MSKUpdateReplicationInfoRequest(BaseModel):
    CurrentVersion: StrictStr
    ReplicatorArn: StrictStr
    ConsumerGroupReplication: MSKConsumerGroupReplicationUpdate | None = None
    SourceKafkaClusterArn: StrictStr | None = None
    SourceKafkaClusterId: StrictStr | None = None
    TargetKafkaClusterArn: StrictStr | None = None
    TargetKafkaClusterId: StrictStr | None = None
    TopicReplication: MSKTopicReplicationUpdate | None = None
    LogDelivery: MSKLogDelivery | None = None
