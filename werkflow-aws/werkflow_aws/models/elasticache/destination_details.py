from pydantic import BaseModel
from .cloud_watch_logs_detail import CloudWatchLogsDetail
from .kinesis_firehose_delivery_detail import KinesisFirehoseDetail


class DestinationDetails(BaseModel):
    CloudWatchLogsDetails: CloudWatchLogsDetail | None = None
    KinesisFirehoseDetails: KinesisFirehoseDetail | None = None