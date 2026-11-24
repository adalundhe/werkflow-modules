from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_s3_destination_description import FirehoseS3DestinationDescription
from .firehose_secrets_manager_configuration import FirehoseSecretsManagerConfiguration
from .firehose_splunk_buffering_hints import FirehoseSplunkBufferingHints
from .firehose_splunk_retry_options import FirehoseSplunkRetryOptions


class FirehoseSplunkDestinationDescription(BaseModel):
    HECEndpoint: StrictStr | None = None
    HECEndpointType: StrictStr | None = None
    HECToken: StrictStr | None = None
    HECAcknowledgmentTimeoutInSeconds: StrictInt | None = None
    RetryOptions: FirehoseSplunkRetryOptions | None = None
    S3BackupMode: StrictStr | None = None
    S3DestinationDescription: FirehoseS3DestinationDescription | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    BufferingHints: FirehoseSplunkBufferingHints | None = None
    SecretsManagerConfiguration: FirehoseSecretsManagerConfiguration | None = None
