import datetime
from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
    StrictBool
)
from typing import Literal, Optional, Dict, List
from .aws_s3_part_response import AWSs3PartResponse


class AWSs3ListPartsResponse(BaseModel):
    AbortDate: Optional[datetime.datetime]=None
    AbortRuleId: Optional[StrictStr]=None
    Bucket: StrictStr
    Key: StrictStr
    UploadId: StrictStr
    PartNumberMarker: StrictInt
    NextPartNumberMarker: StrictInt
    MaxParts: StrictInt
    IsTruncated: StrictBool
    Parts: List[AWSs3PartResponse]=[]
    Initiator: Dict[
        Literal['ID', 'DisplayName'],
        StrictStr
    ]
    Owner: Dict[
        Literal['DisplayName', 'ID'],
        StrictStr
    ]
    StorageClass: Literal[
        'STANDARD',
        'REDUCED_REDUNDANCY',
        'STANDARD_IA',
        'ONEZONE_IA',
        'INTELLIGENT_TIERING',
        'GLACIER',
        'DEEP_ARCHIVE',
        'OUTPOSTS',
        'GLACIER_IR',
        'SNOW',
        'EXPRESS_ONEZONE'
    ]
    RequestCharged: Optional[
        Literal['requester']
    ]=None
    ChecksumAlgorithm: Literal[
        'CRC32',
        'CRC32C',
        'SHA1',
        'SHA256'
    ]