from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .kinesis_enhanced_metrics import KinesisEnhancedMetrics
from .kinesis_shard import KinesisShard
from .kinesis_stream_mode_details import KinesisStreamModeDetails


class KinesisStreamDescription(BaseModel):
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamStatus: StrictStr | None = None
    StreamModeDetails: KinesisStreamModeDetails | None = None
    Shards: list[KinesisShard] | None = None
    HasMoreShards: StrictBool | None = None
    RetentionPeriodHours: StrictInt | None = None
    StreamCreationTimestamp: datetime.datetime | StrictStr | None = None
    EnhancedMonitoring: list[KinesisEnhancedMetrics] | None = None
    EncryptionType: StrictStr | None = None
    KeyId: StrictStr | None = None
