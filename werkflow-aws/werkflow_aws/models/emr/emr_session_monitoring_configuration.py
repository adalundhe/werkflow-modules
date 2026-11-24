from __future__ import annotations
from pydantic import BaseModel
from .emr_session_cloud_watch_logging_configuration import EMRSessionCloudWatchLoggingConfiguration
from .emr_session_managed_logging_configuration import EMRSessionManagedLoggingConfiguration
from .emr_session_s3_logging_configuration import EMRSessionS3LoggingConfiguration


class EMRSessionMonitoringConfiguration(BaseModel):
    CloudWatchLoggingConfiguration: EMRSessionCloudWatchLoggingConfiguration | None = None
    ManagedLoggingConfiguration: EMRSessionManagedLoggingConfiguration | None = None
    S3LoggingConfiguration: EMRSessionS3LoggingConfiguration | None = None
