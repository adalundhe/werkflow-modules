from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_buffering_hints import FirehoseBufferingHints
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_data_format_conversion_configuration import FirehoseDataFormatConversionConfiguration
from .firehose_dynamic_partitioning_configuration import FirehoseDynamicPartitioningConfiguration
from .firehose_encryption_configuration import FirehoseEncryptionConfiguration
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_s3_destination_description import FirehoseS3DestinationDescription


class FirehoseExtendedS3DestinationDescription(BaseModel):
    RoleARN: StrictStr | None = None
    BucketARN: StrictStr | None = None
    Prefix: StrictStr | None = None
    ErrorOutputPrefix: StrictStr | None = None
    BufferingHints: FirehoseBufferingHints | None = None
    CompressionFormat: StrictStr | None = None
    EncryptionConfiguration: FirehoseEncryptionConfiguration | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    S3BackupMode: StrictStr | None = None
    S3BackupDescription: FirehoseS3DestinationDescription | None = None
    DataFormatConversionConfiguration: FirehoseDataFormatConversionConfiguration | None = None
    DynamicPartitioningConfiguration: FirehoseDynamicPartitioningConfiguration | None = None
    FileExtension: StrictStr | None = None
    CustomTimeZone: StrictStr | None = None
