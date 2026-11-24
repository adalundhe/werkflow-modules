from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_s3_destination_update import FirehoseS3DestinationUpdate
from .firehose_secrets_manager_configuration import FirehoseSecretsManagerConfiguration
from .firehose_splunk_buffering_hints import FirehoseSplunkBufferingHints
from .firehose_splunk_retry_options import FirehoseSplunkRetryOptions


class FirehoseSplunkDestinationUpdate(BaseModel):
    HECEndpoint: StrictStr | None = None
    HECEndpointType: Literal['Raw', 'Event'] | None = None
    HECToken: StrictStr | None = None
    HECAcknowledgmentTimeoutInSeconds: StrictInt | None = None
    RetryOptions: FirehoseSplunkRetryOptions | None = None
    S3BackupMode: Literal['FailedEventsOnly', 'AllEvents'] | None = None
    S3Update: FirehoseS3DestinationUpdate | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    BufferingHints: FirehoseSplunkBufferingHints | None = None
    SecretsManagerConfiguration: FirehoseSecretsManagerConfiguration | None = None
