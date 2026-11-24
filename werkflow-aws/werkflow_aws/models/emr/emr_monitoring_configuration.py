from __future__ import annotations
from pydantic import BaseModel
from .emr_cloud_watch_log_configuration import EMRCloudWatchLogConfiguration
from .emrs3_logging_configuration import EMRS3LoggingConfiguration


class EMRMonitoringConfiguration(BaseModel):
    CloudWatchLogConfiguration: EMRCloudWatchLogConfiguration | None = None
    S3LoggingConfiguration: EMRS3LoggingConfiguration | None = None
