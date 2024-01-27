from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
    StrictBool
)

from typing import Literal, Optional, List
from .aws_s3_object_response import AWSs3ObjectResponse
from .aws_s3_common_prefix import AWSs3CommonPrefix


class AWSs3ListObjectsResponse(BaseModel):
    IsTruncated: StrictBool
    Contents: List[AWSs3ObjectResponse]=[]
    Name: StrictStr
    Prefix: StrictStr
    Delimiter: StrictStr
    MaxKeys: StrictInt
    CommonPrefixes: List[AWSs3CommonPrefix]=[]
    EncodingType: Optional[
        Literal['url']
    ]=None
    KeyCount: StrictInt
    ContinuationToken: StrictStr
    NextContinuationToken: StrictStr
    StartAfter: StrictStr
    RequestPayer: Optional[
        Literal['requester']
    ]=None