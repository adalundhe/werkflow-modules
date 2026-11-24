from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_http_endpoint_buffering_hints import FirehoseHttpEndpointBufferingHints
from .firehose_http_endpoint_description import FirehoseHttpEndpointDescription
from .firehose_http_endpoint_request_configuration import FirehoseHttpEndpointRequestConfiguration
from .firehose_http_endpoint_retry_options import FirehoseHttpEndpointRetryOptions
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_s3_destination_description import FirehoseS3DestinationDescription
from .firehose_secrets_manager_configuration import FirehoseSecretsManagerConfiguration


class FirehoseHttpEndpointDestinationDescription(BaseModel):
    EndpointConfiguration: FirehoseHttpEndpointDescription | None = None
    BufferingHints: FirehoseHttpEndpointBufferingHints | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    RequestConfiguration: FirehoseHttpEndpointRequestConfiguration | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    RoleARN: StrictStr | None = None
    RetryOptions: FirehoseHttpEndpointRetryOptions | None = None
    S3BackupMode: StrictStr | None = None
    S3DestinationDescription: FirehoseS3DestinationDescription | None = None
    SecretsManagerConfiguration: FirehoseSecretsManagerConfiguration | None = None
