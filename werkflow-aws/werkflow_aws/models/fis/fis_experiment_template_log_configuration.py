from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .fis_experiment_template_cloud_watch_logs_log_configuration import FISExperimentTemplateCloudWatchLogsLogConfiguration
from .fis_experiment_template_s3_log_configuration import FISExperimentTemplateS3LogConfiguration


class FISExperimentTemplateLogConfiguration(BaseModel):
    cloudWatchLogsConfiguration: FISExperimentTemplateCloudWatchLogsLogConfiguration | None = None
    s3Configuration: FISExperimentTemplateS3LogConfiguration | None = None
    logSchemaVersion: StrictInt | None = None
