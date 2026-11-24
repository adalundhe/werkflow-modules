from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBInputS3Configuration(BaseModel):
    S3BucketOwner: StrictStr | None = None
    S3Bucket: StrictStr | None = None
    S3KeyPrefix: StrictStr | None = None
    InputFormat: StrictStr | None = None
    InputCompressionType: StrictStr | None = None
