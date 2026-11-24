from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .firehose_amazonopensearchservice_buffering_hints import FirehoseAmazonopensearchserviceBufferingHints
from .firehose_amazonopensearchservice_retry_options import FirehoseAmazonopensearchserviceRetryOptions
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_document_id_options import FirehoseDocumentIdOptions
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_s3_destination_configuration import FirehoseS3DestinationConfiguration
from .firehose_vpc_configuration import FirehoseVpcConfiguration


class FirehoseAmazonopensearchserviceDestinationConfiguration(BaseModel):
    RoleARN: StrictStr
    IndexName: StrictStr
    S3Configuration: FirehoseS3DestinationConfiguration
    DomainARN: StrictStr | None = None
    ClusterEndpoint: StrictStr | None = None
    TypeName: StrictStr | None = None
    IndexRotationPeriod: Literal['NoRotation', 'OneHour', 'OneDay', 'OneWeek', 'OneMonth'] | None = None
    BufferingHints: FirehoseAmazonopensearchserviceBufferingHints | None = None
    RetryOptions: FirehoseAmazonopensearchserviceRetryOptions | None = None
    S3BackupMode: Literal['FailedDocumentsOnly', 'AllDocuments'] | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    VpcConfiguration: FirehoseVpcConfiguration | None = None
    DocumentIdOptions: FirehoseDocumentIdOptions | None = None
