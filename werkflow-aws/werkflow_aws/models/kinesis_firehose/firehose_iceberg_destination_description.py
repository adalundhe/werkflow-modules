from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .firehose_buffering_hints import FirehoseBufferingHints
from .firehose_catalog_configuration import FirehoseCatalogConfiguration
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_destination_table_configuration import FirehoseDestinationTableConfiguration
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_retry_options import FirehoseRetryOptions
from .firehose_s3_destination_description import FirehoseS3DestinationDescription
from .firehose_schema_evolution_configuration import FirehoseSchemaEvolutionConfiguration
from .firehose_table_creation_configuration import FirehoseTableCreationConfiguration


class FirehoseIcebergDestinationDescription(BaseModel):
    DestinationTableConfigurationList: list[FirehoseDestinationTableConfiguration] | None = None
    SchemaEvolutionConfiguration: FirehoseSchemaEvolutionConfiguration | None = None
    TableCreationConfiguration: FirehoseTableCreationConfiguration | None = None
    BufferingHints: FirehoseBufferingHints | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    S3BackupMode: StrictStr | None = None
    RetryOptions: FirehoseRetryOptions | None = None
    RoleARN: StrictStr | None = None
    AppendOnly: StrictBool | None = None
    CatalogConfiguration: FirehoseCatalogConfiguration | None = None
    S3DestinationDescription: FirehoseS3DestinationDescription | None = None
