from pydantic import BaseModel
from .elasticache_cloud_watch_logs_detail import ElasticacheCloudWatchLogsDetail
from .elasticache_kinesis_firehose_delivery_detail import ElasticacheKinesisFirehoseDetail


class ElasticacheDestinationDetails(BaseModel):
    CloudWatchLogsDetails: ElasticacheCloudWatchLogsDetail | None = None
    KinesisFirehoseDetails: ElasticacheKinesisFirehoseDetail | None = None