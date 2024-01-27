from pydantic import (
    StrictStr,
    StrictBool
)
from werkflow_aws.models.base import AWSBoto3Base
from typing import Optional, Literal


class AWSs3DeleteObjectsOptions(AWSBoto3Base):
    mfa: Optional[StrictStr]=None
    request_payer: Optional[
        Literal['requester']
    ]=None
    bypass_governance_retention: Optional[StrictBool]=None
    expected_bucket_owner: Optional[StrictStr]=None
    checksum_algorithm: Optional[
        Literal[
            'CRC32',
            'CRC32C',
            'SHA1',
            'SHA256'
        ]
    ]=None