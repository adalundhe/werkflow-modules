from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .msk_consumer_group_replication import MSKConsumerGroupReplication
from .msk_topic_replication import MSKTopicReplication


class MSKReplicationInfo(BaseModel):
    ConsumerGroupReplication: MSKConsumerGroupReplication
    TargetCompressionType: Literal['NONE', 'GZIP', 'SNAPPY', 'LZ4', 'ZSTD']
    TopicReplication: MSKTopicReplication
    SourceKafkaClusterArn: StrictStr | None = None
    SourceKafkaClusterId: StrictStr | None = None
    TargetKafkaClusterArn: StrictStr | None = None
    TargetKafkaClusterId: StrictStr | None = None
