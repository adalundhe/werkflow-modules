from pydantic import BaseModel
from .msk_cloudwatch_logs import MSKCloudWatchLogs
from .msk_firehose import MSKFirehose
from .msk_s3 import MSKS3


class MSKBrokerLogs(BaseModel):
    CloudWatchLogs: MSKCloudWatchLogs
    Firehose: MSKFirehose
    S3: MSKS3