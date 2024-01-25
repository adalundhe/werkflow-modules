from pydantic import (
    StrictBool,
    StrictStr,
    StrictInt
)

from typing import Optional, List
from werkflow_aws.models.base import AWSBoto3Options


class AWSs3DeleteBucketOptions(AWSBoto3Options):
    expected_bucket_owner: Optional[StrictStr]

