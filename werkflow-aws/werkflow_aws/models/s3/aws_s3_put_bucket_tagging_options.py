from pydantic import (
    StrictStr
)
from typing import Literal, Optional
from werkflow_aws.models.base import AWSBoto3Base


class AWSs3PutBucketTaggingOptions(AWSBoto3Base):
    checksum_algorithm: Optional[
        Literal[
            'CRC32',
            'CRC32C',
            'SHA1',
            'SHA256'
        ]
    ]=None
    expected_bucket_owner: Optional[StrictStr]=None