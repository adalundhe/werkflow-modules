from pydantic import StrictStr
from werkflow_aws.models.base import AWSBoto3Options
from typing import Optional, Literal


class AWSs3AbortMultipartUploadOptions(AWSBoto3Options):
    request_payer: Optional[
        Literal['requester']
    ]=None
    expected_bucket_owner: Optional[StrictStr]=None