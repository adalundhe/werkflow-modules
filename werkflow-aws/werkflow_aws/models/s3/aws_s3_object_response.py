import datetime
from typing import Dict, List, Literal
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr


class AWSs3ObjectResponse(BaseModel):
    Key: StrictStr | None = None
    LastModified: datetime.datetime | None = None
    ETag: StrictStr | None = None
    ChecksumAlgorithm: List[Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256']] = Field(
        default_factory=list
    )
    Size: StrictInt | None = None
    StorageClass: Literal[
        'STANDARD',
        'REDUCED_REDUNDANCY',
        'GLACIER',
        'STANDARD_IA',
        'ONEZONE_IA',
        'INTELLIGENT_TIERING',
        'DEEP_ARCHIVE',
        'OUTPOSTS',
        'GLACIER_IR',
        'SNOW',
        'EXPRESS_ONEZONE',
    ] | None = None
    Owner: Dict[Literal['DisplayName', 'ID'], StrictStr] | None = None
    RestoreStatus: Dict[
        Literal['IsRestoreInProgress', 'RestoreExpiryDate'],
        StrictBool | datetime.datetime,
    ] | None = None
