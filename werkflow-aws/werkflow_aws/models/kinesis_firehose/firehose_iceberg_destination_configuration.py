from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .firehose_buffering_hints import FirehoseBufferingHints
from .firehose_catalog_configuration import FirehoseCatalogConfiguration
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_destination_table_configuration import FirehoseDestinationTableConfiguration
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_retry_options import FirehoseRetryOptions
from .firehose_s3_destination_configuration import FirehoseS3DestinationConfiguration
from .firehose_schema_evolution_configuration import FirehoseSchemaEvolutionConfiguration
from .firehose_table_creation_configuration import FirehoseTableCreationConfiguration


class FirehoseIcebergDestinationConfiguration(BaseModel):
    RoleARN: StrictStr
    CatalogConfiguration: FirehoseCatalogConfiguration
    S3Configuration: FirehoseS3DestinationConfiguration
    DestinationTableConfigurationList: list[FirehoseDestinationTableConfiguration] | None = None
    SchemaEvolutionConfiguration: FirehoseSchemaEvolutionConfiguration | None = None
    TableCreationConfiguration: FirehoseTableCreationConfiguration | None = None
    BufferingHints: FirehoseBufferingHints | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    S3BackupMode: Literal['FailedDataOnly', 'AllData'] | None = None
    RetryOptions: FirehoseRetryOptions | None = None
    AppendOnly: StrictBool | None = None
