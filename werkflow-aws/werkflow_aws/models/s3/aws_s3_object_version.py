import datetime
from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
    StrictBool
)
from werkflow_aws.models.base import AWSBoto3Base
from typing import Literal, Dict, List


class AWSs3ObjectVersion(AWSBoto3Base):
    e_tag: StrictStr
    checksum_algorithm: List[
        Literal[
            'CRC32',
            'CRC32C',
            'SHA1',
            'SHA256'
        ]
    ]=[]
    size: StrictInt
    storage_class: Literal[
        'STANDARD'
    ]
    key: StrictStr
    version_id: StrictStr
    is_latest: StrictBool
    last_modified: datetime.datetime
    owner: Dict[
        Literal[
            'DisplayName',
            'ID'
        ],
        StrictStr
    ]
    restore_status: Dict[
        Literal[
            'IsRestoreInProgress',
            'RestoreExpiryDate'
        ],
        StrictStr
    ]