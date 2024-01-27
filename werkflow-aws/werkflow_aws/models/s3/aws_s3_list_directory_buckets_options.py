from pydantic import (
    StrictStr
)

from typing import Optional
from werkflow_aws.models.base import AWSBoto3Base


class AWSs3ListDirectoryBucketsOptions(AWSBoto3Base):
    continuation_token: Optional[StrictStr]=None
    max_directory_buckets: Optional[StrictStr]=None
