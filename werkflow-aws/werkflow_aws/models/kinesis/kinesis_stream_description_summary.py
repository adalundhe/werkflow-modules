from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_enhanced_metrics import KinesisEnhancedMetrics
from .kinesis_stream_mode_details import KinesisStreamModeDetails
from .kinesis_warm_throughput_object import KinesisWarmThroughputObject


class KinesisStreamDescriptionSummary(BaseModel):
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
    StreamStatus: StrictStr | None = None
    StreamModeDetails: KinesisStreamModeDetails | None = None
    RetentionPeriodHours: StrictInt | None = None
    StreamCreationTimestamp: datetime.datetime | StrictStr | None = None
    EnhancedMonitoring: list[KinesisEnhancedMetrics] | None = None
    EncryptionType: StrictStr | None = None
    KeyId: StrictStr | None = None
    OpenShardCount: StrictInt | None = None
    ConsumerCount: StrictInt | None = None
    WarmThroughput: KinesisWarmThroughputObject | None = None
    MaxRecordSizeInKiB: StrictInt | None = None
    ChannelCount: StrictInt | None = None
    RecordDistributionStrategy: StrictStr | None = None
    QueueCount: StrictInt | None = None
