from typing import List, Literal, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from .aws_s3_common_prefix import AWSs3CommonPrefix
from .aws_s3_delete_marker import AWSs3DeleteMarker
from .aws_s3_object_version import AWSs3ObjectVersion


class AWSs3ListObjectVersionsResponse(BaseModel):
    IsTruncated: StrictBool | None = None
    KeyMarker: StrictStr | None = None
    VersionIdMarker: StrictStr | None = None
    NextKeyMarker: StrictStr | None = None
    NextVersionIdMarker: StrictStr | None = None
    Versions: List[AWSs3ObjectVersion] = Field(default_factory=list)
    DeleteMarkers: List[AWSs3DeleteMarker] = Field(default_factory=list)
    Name: StrictStr | None = None
    Prefix: StrictStr | None = None
    Delimiter: StrictStr | None = None
    MaxKeys: StrictInt | None = None
    CommonPrefixes: List[AWSs3CommonPrefix] = Field(default_factory=list)
    EncodingType: Optional[Literal['url']] = None
    RequestCharged: Optional[Literal['requester']] = None
