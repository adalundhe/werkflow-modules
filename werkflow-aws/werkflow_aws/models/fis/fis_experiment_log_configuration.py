from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .fis_experiment_cloud_watch_logs_log_configuration import FISExperimentCloudWatchLogsLogConfiguration
from .fis_experiment_s3_log_configuration import FISExperimentS3LogConfiguration


class FISExperimentLogConfiguration(BaseModel):
    cloudWatchLogsConfiguration: FISExperimentCloudWatchLogsLogConfiguration | None = None
    s3Configuration: FISExperimentS3LogConfiguration | None = None
    logSchemaVersion: StrictInt | None = None
