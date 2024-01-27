import datetime
from pydantic import (
    BaseModel,
    StrictStr
)
from typing import Dict, Literal


class AWSs3MultipartUploadResponse(BaseModel):
    UploadId: StrictStr
    Key: StrictStr
    Initiated: datetime.datetime
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
    Owner: Dict[
        Literal['DisplayName', 'ID'],
        StrictStr
    ]
    Initiator: Dict[
        Literal[
            'ID',
            'DisplayName'
        ],
        StrictStr
    ]
    ChecksumAlgorithm: Literal[
        'CRC32',
        'CRC32C',
        'SHA1',
        'SHA256'
    ]