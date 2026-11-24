from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_document_id_options import FirehoseDocumentIdOptions
from .firehose_elasticsearch_buffering_hints import FirehoseElasticsearchBufferingHints
from .firehose_elasticsearch_retry_options import FirehoseElasticsearchRetryOptions
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_s3_destination_update import FirehoseS3DestinationUpdate


class FirehoseElasticsearchDestinationUpdate(BaseModel):
    RoleARN: StrictStr | None = None
    DomainARN: StrictStr | None = None
    ClusterEndpoint: StrictStr | None = None
    IndexName: StrictStr | None = None
    TypeName: StrictStr | None = None
    IndexRotationPeriod: Literal['NoRotation', 'OneHour', 'OneDay', 'OneWeek', 'OneMonth'] | None = None
    BufferingHints: FirehoseElasticsearchBufferingHints | None = None
    RetryOptions: FirehoseElasticsearchRetryOptions | None = None
    S3Update: FirehoseS3DestinationUpdate | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    DocumentIdOptions: FirehoseDocumentIdOptions | None = None
