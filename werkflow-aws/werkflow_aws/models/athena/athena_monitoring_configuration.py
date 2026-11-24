from __future__ import annotations
from pydantic import BaseModel
from .athena_cloud_watch_logging_configuration import AthenaCloudWatchLoggingConfiguration
from .athena_managed_logging_configuration import AthenaManagedLoggingConfiguration
from .athena_s3_logging_configuration import AthenaS3LoggingConfiguration


class AthenaMonitoringConfiguration(BaseModel):
    CloudWatchLoggingConfiguration: AthenaCloudWatchLoggingConfiguration | None = None
    ManagedLoggingConfiguration: AthenaManagedLoggingConfiguration | None = None
    S3LoggingConfiguration: AthenaS3LoggingConfiguration | None = None
