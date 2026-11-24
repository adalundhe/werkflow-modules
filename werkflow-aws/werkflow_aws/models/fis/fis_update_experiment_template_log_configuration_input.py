from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .fis_experiment_template_cloud_watch_logs_log_configuration_input import FISExperimentTemplateCloudWatchLogsLogConfigurationInput
from .fis_experiment_template_s3_log_configuration_input import FISExperimentTemplateS3LogConfigurationInput


class FISUpdateExperimentTemplateLogConfigurationInput(BaseModel):
    cloudWatchLogsConfiguration: FISExperimentTemplateCloudWatchLogsLogConfigurationInput | None = None
    s3Configuration: FISExperimentTemplateS3LogConfigurationInput | None = None
    logSchemaVersion: StrictInt | None = None
