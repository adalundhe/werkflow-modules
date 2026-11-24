from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_serverless_stream_bucket_config import OpenSearchServerlessStreamBucketConfig


class OpenSearchServerlessIngestionStreamS3Source(BaseModel):
    sqsArn: StrictStr | None = None
    buckets: list[OpenSearchServerlessStreamBucketConfig] | None = None
