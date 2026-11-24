from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBOutputS3Configuration(BaseModel):
    S3BucketOwner: StrictStr | None = None
    S3Bucket: StrictStr | None = None
    S3KeyPrefix: StrictStr | None = None
    S3SseAlgorithm: StrictStr | None = None
    S3SseKmsKeyId: StrictStr | None = None
    OutputType: list[StrictStr] | None = None
