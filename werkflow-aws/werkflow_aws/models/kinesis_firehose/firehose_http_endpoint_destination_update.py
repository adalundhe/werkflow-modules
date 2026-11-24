from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_http_endpoint_buffering_hints import FirehoseHttpEndpointBufferingHints
from .firehose_http_endpoint_configuration import FirehoseHttpEndpointConfiguration
from .firehose_http_endpoint_request_configuration import FirehoseHttpEndpointRequestConfiguration
from .firehose_http_endpoint_retry_options import FirehoseHttpEndpointRetryOptions
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_s3_destination_update import FirehoseS3DestinationUpdate
from .firehose_secrets_manager_configuration import FirehoseSecretsManagerConfiguration


class FirehoseHttpEndpointDestinationUpdate(BaseModel):
    EndpointConfiguration: FirehoseHttpEndpointConfiguration | None = None
    BufferingHints: FirehoseHttpEndpointBufferingHints | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    RequestConfiguration: FirehoseHttpEndpointRequestConfiguration | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    RoleARN: StrictStr | None = None
    RetryOptions: FirehoseHttpEndpointRetryOptions | None = None
    S3BackupMode: Literal['FailedDataOnly', 'AllData'] | None = None
    S3Update: FirehoseS3DestinationUpdate | None = None
    SecretsManagerConfiguration: FirehoseSecretsManagerConfiguration | None = None
