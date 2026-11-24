import datetime
from typing import Dict, List, Literal, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from .aws_s3_part_response import AWSs3PartResponse


class AWSs3ListPartsResponse(BaseModel):
    AbortDate: Optional[datetime.datetime] = None
    AbortRuleId: Optional[StrictStr] = None
    Bucket: StrictStr | None = None
    Key: StrictStr | None = None
    UploadId: StrictStr | None = None
    PartNumberMarker: StrictInt | None = None
    NextPartNumberMarker: StrictInt | None = None
    MaxParts: StrictInt | None = None
    IsTruncated: StrictBool | None = None
    Parts: List[AWSs3PartResponse] = Field(default_factory=list)
    Initiator: Dict[Literal['ID', 'DisplayName'], StrictStr] | None = None
    Owner: Dict[Literal['DisplayName', 'ID'], StrictStr] | None = None
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
        'EXPRESS_ONEZONE',
    ] | None = None
    RequestCharged: Optional[Literal['requester']] = None
    ChecksumAlgorithm: Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256'] | None = None
