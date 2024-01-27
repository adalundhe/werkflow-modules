from pydantic import (
    BaseModel,
    StrictStr,
    StrictBool,
    StrictInt
)
from typing import List, Literal, Optional
from .aws_s3_common_prefix import AWSs3CommonPrefix
from .aws_s3_delete_marker import AWSs3DeleteMarker
from .aws_s3_object_version import AWSs3ObjectVersion


class AWSs3ListObjectVersionsResponse(BaseModel):
    IsTruncated: StrictBool
    KeyMarker: StrictStr
    VersionIdMarker: StrictStr
    NextKeyMarker: StrictStr
    NextVersionIdMarker: StrictStr
    Versions: List[AWSs3ObjectVersion]=[]
    DeleteMarkers: List[AWSs3DeleteMarker]=[]
    Name: StrictStr
    Prefix: StrictStr
    Delimiter: StrictStr
    MaxKeys: StrictInt
    CommonPrefixes: List[AWSs3CommonPrefix]=[]
    EncodingType: Optional[
        Literal['url']
    ]=None
    ReqeustCharged: Optional[
        Literal['requester']
    ]=None