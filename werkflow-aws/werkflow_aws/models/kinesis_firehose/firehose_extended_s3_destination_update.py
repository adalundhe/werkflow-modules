from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .firehose_buffering_hints import FirehoseBufferingHints
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_data_format_conversion_configuration import FirehoseDataFormatConversionConfiguration
from .firehose_dynamic_partitioning_configuration import FirehoseDynamicPartitioningConfiguration
from .firehose_encryption_configuration import FirehoseEncryptionConfiguration
from .firehose_processing_configuration import FirehoseProcessingConfiguration
from .firehose_s3_destination_update import FirehoseS3DestinationUpdate


class FirehoseExtendedS3DestinationUpdate(BaseModel):
    RoleARN: StrictStr | None = None
    BucketARN: StrictStr | None = None
    Prefix: StrictStr | None = None
    ErrorOutputPrefix: StrictStr | None = None
    BufferingHints: FirehoseBufferingHints | None = None
    CompressionFormat: Literal['UNCOMPRESSED', 'GZIP', 'ZIP', 'Snappy', 'HADOOP_SNAPPY'] | None = None
    EncryptionConfiguration: FirehoseEncryptionConfiguration | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
    ProcessingConfiguration: FirehoseProcessingConfiguration | None = None
    S3BackupMode: Literal['Disabled', 'Enabled'] | None = None
    S3BackupUpdate: FirehoseS3DestinationUpdate | None = None
    DataFormatConversionConfiguration: FirehoseDataFormatConversionConfiguration | None = None
    DynamicPartitioningConfiguration: FirehoseDynamicPartitioningConfiguration | None = None
    FileExtension: StrictStr | None = None
    CustomTimeZone: StrictStr | None = None
