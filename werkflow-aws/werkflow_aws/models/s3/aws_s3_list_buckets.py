from pydantic import BaseModel, Field
from typing import List
from .aws_s3_bucket_response import AWSs3BucketResponse
from .aws_s3_owner_response import AWSs3OwnerResponse


class AWSs3ListBucketsResponse(BaseModel):
    Buckets: List[AWSs3BucketResponse] = Field(default_factory=list)
    Owner: AWSs3OwnerResponse | None = None
