from typing import List, Literal, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from .aws_s3_common_prefix import AWSs3CommonPrefix
from .aws_s3_object_response import AWSs3ObjectResponse


class AWSS3ListObjectsResponse(BaseModel):
    IsTruncated: StrictBool | None = None
    Contents: List[AWSs3ObjectResponse] = Field(default_factory=list)
    Name: StrictStr | None = None
    Prefix: StrictStr | None = None
    Delimiter: StrictStr | None = None
    MaxKeys: StrictInt | None = None
    CommonPrefixes: List[AWSs3CommonPrefix] = Field(default_factory=list)
    EncodingType: Optional[Literal['url']] = None
    KeyCount: StrictInt | None = None
    ContinuationToken: StrictStr | None = None
    NextContinuationToken: StrictStr | None = None
    StartAfter: StrictStr | None = None
    RequestCharged: Optional[Literal['requester']] = None
