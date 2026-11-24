from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .firehose_amazon_open_search_serverless_buffering_hints import FirehoseAmazonOpenSearchServerlessBufferingHints
from .firehose_amazon_open_search_serverless_retry_options import FirehoseAmazonOpenSearchServerlessRetryOptions
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_s3_destination_configuration import FirehoseS3DestinationConfiguration
from .firehose_vpc_configuration import FirehoseVpcConfiguration


class FirehoseAmazonOpenSearchServerlessDestinationConfiguration(BaseModel):
    RoleARN: StrictStr
    IndexName: StrictStr
    S3Configuration: FirehoseS3DestinationConfiguration
    CollectionEndpoint: StrictStr | None = None
    BufferingHints: FirehoseAmazonOpenSearchServerlessBufferingHints | None = None
    RetryOptions: FirehoseAmazonOpenSearchServerlessRetryOptions | None = None
    S3BackupMode: Literal['FailedDocumentsOnly', 'AllDocuments'] | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    VpcConfiguration: FirehoseVpcConfiguration | None = None
