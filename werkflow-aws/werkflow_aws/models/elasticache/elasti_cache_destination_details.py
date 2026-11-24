from __future__ import annotations
from pydantic import BaseModel
from .elasti_cache_cloud_watch_logs_destination_details import ElastiCacheCloudWatchLogsDestinationDetails
from .elasti_cache_kinesis_firehose_destination_details import ElastiCacheKinesisFirehoseDestinationDetails


class ElastiCacheDestinationDetails(BaseModel):
    CloudWatchLogsDetails: ElastiCacheCloudWatchLogsDestinationDetails | None = None
    KinesisFirehoseDetails: ElastiCacheKinesisFirehoseDestinationDetails | None = None
