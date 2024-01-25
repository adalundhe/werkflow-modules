from pydantic import (
    StrictBool,
    StrictStr,
    StrictInt
)

from typing import Optional, List
from werkflow_aws.models.base import AWSBoto3Options


class AWSs3ListMultipartUploadOptions(AWSBoto3Options):
    delimiter: Optional[StrictStr]
    encoding_type: Optional[StrictStr]
    key_marker: Optional[StrictStr]
    max_uploads: Optional[StrictInt]
    prefix: Optional[StrictStr]
    upload_id_marker: Optional[StrictStr]
    expected_bucket_owner: Optional[StrictStr]
