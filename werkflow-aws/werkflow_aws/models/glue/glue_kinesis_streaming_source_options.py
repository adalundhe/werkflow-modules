from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class GlueKinesisStreamingSourceOptions(BaseModel):
    EndpointUrl: StrictStr | None = None
    StreamName: StrictStr | None = None
    Classification: StrictStr | None = None
    Delimiter: StrictStr | None = None
    StartingPosition: StrictStr | None = None
    MaxFetchTimeInMs: StrictInt | None = None
    MaxFetchRecordsPerShard: StrictInt | None = None
    MaxRecordPerRead: StrictInt | None = None
    AddIdleTimeBetweenReads: StrictBool | None = None
    IdleTimeBetweenReadsInMs: StrictInt | None = None
    DescribeShardInterval: StrictInt | None = None
    NumRetries: StrictInt | None = None
    RetryIntervalMs: StrictInt | None = None
    MaxRetryIntervalMs: StrictInt | None = None
    AvoidEmptyBatches: StrictBool | None = None
    StreamArn: StrictStr | None = None
    RoleArn: StrictStr | None = None
    RoleSessionName: StrictStr | None = None
    AddRecordTimestamp: StrictStr | None = None
    EmitConsumerLagMetrics: StrictStr | None = None
    StartingTimestamp: datetime.datetime | StrictStr | None = None
    FanoutConsumerARN: StrictStr | None = None
