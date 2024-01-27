import datetime
from pydantic import BaseModel, StrictStr, StrictInt, StrictBool
from typing import List, Optional, Literal
from .aws_s3_common_prefix import AWSs3CommonPrefix
from .aws_s3_multipart_upload_response import AWSs3MultipartUploadResponse


class AWSs3ListMultipartUploadsResponse(BaseModel):
    Bucket: StrictStr
    KeyMarker: StrictStr
    UploadIdMarker: StrictStr
    NextKeyMarker: StrictStr
    Premix: StrictStr
    Delimiter: StrictStr
    NextUploadIdMarker: StrictStr
    MaxUploads: StrictInt
    IsTruncated: StrictBool
    Uploads: List[AWSs3MultipartUploadResponse]=[]
    CommonPrefixes: List[AWSs3CommonPrefix]=[]
    EncodingType: Optional[
        Literal['url']
    ]=None
    RequestCharged: Optional[
        Literal['requester']
    ]=None
