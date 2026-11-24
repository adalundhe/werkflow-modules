from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .firehose_buffering_hints import FirehoseBufferingHints
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_encryption_configuration import FirehoseEncryptionConfiguration


class FirehoseS3DestinationConfiguration(BaseModel):
    RoleARN: StrictStr
    BucketARN: StrictStr
    Prefix: StrictStr | None = None
    ErrorOutputPrefix: StrictStr | None = None
    BufferingHints: FirehoseBufferingHints | None = None
    CompressionFormat: Literal['UNCOMPRESSED', 'GZIP', 'ZIP', 'Snappy', 'HADOOP_SNAPPY'] | None = None
    EncryptionConfiguration: FirehoseEncryptionConfiguration | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
