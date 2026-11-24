from typing import List, Literal, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from .aws_s3_common_prefix import AWSs3CommonPrefix
from .aws_s3_multipart_upload_response import AWSs3MultipartUploadResponse


class AWSs3ListMultipartUploadsResponse(BaseModel):
    Bucket: StrictStr | None = None
    KeyMarker: StrictStr | None = None
    UploadIdMarker: StrictStr | None = None
    NextKeyMarker: StrictStr | None = None
    Prefix: StrictStr | None = None
    Delimiter: StrictStr | None = None
    NextUploadIdMarker: StrictStr | None = None
    MaxUploads: StrictInt | None = None
    IsTruncated: StrictBool | None = None
    Uploads: List[AWSs3MultipartUploadResponse] = Field(default_factory=list)
    CommonPrefixes: List[AWSs3CommonPrefix] = Field(default_factory=list)
    EncodingType: Optional[Literal['url']] = None
    RequestCharged: Optional[Literal['requester']] = None
