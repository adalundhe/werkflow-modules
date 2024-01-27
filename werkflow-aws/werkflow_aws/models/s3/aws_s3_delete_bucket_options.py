from pydantic import (
    StrictStr
)

from typing import Optional
from werkflow_aws.models.base import AWSBoto3Options


class AWSs3DeleteBucketOptions(AWSBoto3Options):
    expected_bucket_owner: Optional[StrictStr]=None

