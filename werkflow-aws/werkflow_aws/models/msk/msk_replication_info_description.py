from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .msk_consumer_group_replication import MSKConsumerGroupReplication
from .msk_topic_replication import MSKTopicReplication


class MSKReplicationInfoDescription(BaseModel):
    ConsumerGroupReplication: MSKConsumerGroupReplication | None = None
    SourceKafkaClusterAlias: StrictStr | None = None
    TargetCompressionType: StrictStr | None = None
    TargetKafkaClusterAlias: StrictStr | None = None
    TopicReplication: MSKTopicReplication | None = None
