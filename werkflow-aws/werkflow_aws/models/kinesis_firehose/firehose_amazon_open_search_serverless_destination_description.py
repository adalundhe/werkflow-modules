from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_amazon_open_search_serverless_buffering_hints import FirehoseAmazonOpenSearchServerlessBufferingHints
from .firehose_amazon_open_search_serverless_retry_options import FirehoseAmazonOpenSearchServerlessRetryOptions
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_s3_destination_description import FirehoseS3DestinationDescription
from .firehose_vpc_configuration_description import FirehoseVpcConfigurationDescription


class FirehoseAmazonOpenSearchServerlessDestinationDescription(BaseModel):
    RoleARN: StrictStr | None = None
    CollectionEndpoint: StrictStr | None = None
    IndexName: StrictStr | None = None
    BufferingHints: FirehoseAmazonOpenSearchServerlessBufferingHints | None = None
    RetryOptions: FirehoseAmazonOpenSearchServerlessRetryOptions | None = None
    S3BackupMode: StrictStr | None = None
    S3DestinationDescription: FirehoseS3DestinationDescription | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    VpcConfigurationDescription: FirehoseVpcConfigurationDescription | None = None
