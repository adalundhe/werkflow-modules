from pydantic import (
    BaseModel
)
from typing import List
from .aws_s3_tag import AWSs3Tag


class AWSs3GetBucketTaggingResponse(BaseModel):
    TagSet: List[AWSs3Tag]=[]