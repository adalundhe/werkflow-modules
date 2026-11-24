from __future__ import annotations
from pydantic import BaseModel
from .msk_cloud_watch_logs_model import MSKCloudWatchLogsModel
from .msk_firehose_model import MSKFirehoseModel
from .msks3_model import MSKS3Model


class MSKBrokerLogsModel(BaseModel):
    CloudWatchLogs: MSKCloudWatchLogsModel | None = None
    Firehose: MSKFirehoseModel | None = None
    S3: MSKS3Model | None = None
