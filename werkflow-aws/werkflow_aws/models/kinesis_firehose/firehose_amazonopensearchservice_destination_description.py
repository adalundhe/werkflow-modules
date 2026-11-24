from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_amazonopensearchservice_buffering_hints import FirehoseAmazonopensearchserviceBufferingHints
from .firehose_amazonopensearchservice_retry_options import FirehoseAmazonopensearchserviceRetryOptions
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_document_id_options import FirehoseDocumentIdOptions
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_s3_destination_description import FirehoseS3DestinationDescription
from .firehose_vpc_configuration_description import FirehoseVpcConfigurationDescription


class FirehoseAmazonopensearchserviceDestinationDescription(BaseModel):
    RoleARN: StrictStr | None = None
    DomainARN: StrictStr | None = None
    ClusterEndpoint: StrictStr | None = None
    IndexName: StrictStr | None = None
    TypeName: StrictStr | None = None
    IndexRotationPeriod: StrictStr | None = None
    BufferingHints: FirehoseAmazonopensearchserviceBufferingHints | None = None
    RetryOptions: FirehoseAmazonopensearchserviceRetryOptions | None = None
    S3BackupMode: StrictStr | None = None
    S3DestinationDescription: FirehoseS3DestinationDescription | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    VpcConfigurationDescription: FirehoseVpcConfigurationDescription | None = None
    DocumentIdOptions: FirehoseDocumentIdOptions | None = None
