from pydantic import (
    BaseModel,
    StrictStr
)
from typing import List
from .aws_s3_tag import AWSs3Tag


class AWSs3GetObjectTaggingResponse(BaseModel):
    VersionId: StrictStr
    TagSet: List[AWSs3Tag]=[]