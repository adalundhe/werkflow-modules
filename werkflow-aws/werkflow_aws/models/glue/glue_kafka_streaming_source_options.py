from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class GlueKafkaStreamingSourceOptions(BaseModel):
    BootstrapServers: StrictStr | None = None
    SecurityProtocol: StrictStr | None = None
    ConnectionName: StrictStr | None = None
    TopicName: StrictStr | None = None
    Assign: StrictStr | None = None
    SubscribePattern: StrictStr | None = None
    Classification: StrictStr | None = None
    Delimiter: StrictStr | None = None
    StartingOffsets: StrictStr | None = None
    EndingOffsets: StrictStr | None = None
    PollTimeoutMs: StrictInt | None = None
    NumRetries: StrictInt | None = None
    RetryIntervalMs: StrictInt | None = None
    MaxOffsetsPerTrigger: StrictInt | None = None
    MinPartitions: StrictInt | None = None
    IncludeHeaders: StrictBool | None = None
    AddRecordTimestamp: StrictStr | None = None
    EmitConsumerLagMetrics: StrictStr | None = None
    StartingTimestamp: datetime.datetime | StrictStr | None = None
