from pydantic import (
    StrictBool,
    StrictStr,
    StrictInt
)

from typing import Optional, List
from werkflow_aws.models.base import AWSBoto3Base


class AWSs3ListObjectsOptions(AWSBoto3Base):
    delimiter: Optional[StrictStr]=None
    encoding_type: Optional[StrictStr]=None
    max_keys: Optional[StrictInt]=None
    prefix: Optional[StrictStr]=None
    continuation_token: Optional[StrictStr]=None
    fetch_owner: Optional[StrictBool]=None
    start_after: Optional[StrictStr]=None
    expected_bucket_owner: Optional[StrictStr]=None
    optional_object_attributes: Optional[List[StrictStr]]=None

