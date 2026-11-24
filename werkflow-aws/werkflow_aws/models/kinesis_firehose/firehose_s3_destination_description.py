from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .firehose_buffering_hints import FirehoseBufferingHints
from .firehose_cloud_watch_logging_options import FirehoseCloudWatchLoggingOptions
from .firehose_encryption_configuration import FirehoseEncryptionConfiguration


class FirehoseS3DestinationDescription(BaseModel):
    RoleARN: StrictStr | None = None
    BucketARN: StrictStr | None = None
    Prefix: StrictStr | None = None
    ErrorOutputPrefix: StrictStr | None = None
    BufferingHints: FirehoseBufferingHints | None = None
    CompressionFormat: StrictStr | None = None
    EncryptionConfiguration: FirehoseEncryptionConfiguration | None = None
    CloudWatchLoggingOptions: FirehoseCloudWatchLoggingOptions | None = None
