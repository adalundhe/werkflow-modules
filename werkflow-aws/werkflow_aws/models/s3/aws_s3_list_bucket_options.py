from pydantic import (
    StrictBool,
    StrictStr,
    StrictInt
)

from typing import Optional, List
from werkflow_aws.models.base import AWSBoto3Options


class AWSs3ListBucketOptions(AWSBoto3Options):
    delimiter: Optional[StrictStr]
    encoding_type: Optional[StrictStr]
    max_keys: Optional[StrictInt]
    prefix: Optional[StrictStr]
    continuation_token: Optional[StrictStr]
    fetch_owner: Optional[StrictBool]
    start_after: Optional[StrictStr]
    expected_bucket_owner: Optional[StrictStr]
    optional_object_attributes: Optional[List[StrictStr]]

