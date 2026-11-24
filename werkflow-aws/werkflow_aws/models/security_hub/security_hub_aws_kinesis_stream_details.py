from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_kinesis_stream_stream_encryption_details import SecurityHubAwsKinesisStreamStreamEncryptionDetails


class SecurityHubAwsKinesisStreamDetails(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    StreamEncryption: SecurityHubAwsKinesisStreamStreamEncryptionDetails | None = None
    ShardCount: StrictInt | None = None
    RetentionPeriodHours: StrictInt | None = None
