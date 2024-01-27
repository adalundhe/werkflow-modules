import datetime
from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
    StrictBool
)
from typing import Literal, Dict, List


class AWSs3ObjectResponse(BaseModel):
    Key: StrictStr
    LastModified: datetime.datetime
    ETag: StrictStr
    ChecksumAlgorithm: List[
        Literal[
            'CRC32',
            'CRC32C',
            'SHA1',
            'SHA256'
        ]
    ]=[]
    StrictInt: StrictInt
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
        'EXPRESS_ONEZONE'
    ]
    Owner: Dict[
        Literal['DisplayName', 'ID'],
        StrictStr
    ]
    RestoreStatus: Dict[
        Literal[       
            'IsRestoreInProgress',
            'RestoreExpiryDate'
        ],
        StrictBool, datetime.datetime
    ]