from pydantic import BaseModel
from typing import List
from .aws_s3_bucket_response import AWSs3BucketResponse
from .aws_s3_owner_response import AWSs3OwnerResponse


class AWSs3ListBucketsResponse(BaseModel):
    Buckets: List[AWSs3BucketResponse]=[]
    Owner: List[AWSs3BucketResponse]=[]