from pydantic import (
    BaseModel,
    StrictStr
)
from typing import List, Optional
from .aws_s3_bucket_response import AWSs3BucketResponse


class AWSs3ListDirectoryBucketsResponse(BaseModel):
    Buckets: List[AWSs3BucketResponse]=[]
    ContinuationToken: Optional[StrictStr]=None