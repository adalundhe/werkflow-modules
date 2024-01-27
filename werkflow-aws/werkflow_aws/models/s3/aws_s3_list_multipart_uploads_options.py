from pydantic import (
    StrictStr,
    StrictInt
)

from typing import Optional
from werkflow_aws.models.base import AWSBoto3Base


class AWSs3ListMultipartUploadsOptions(AWSBoto3Base):
    delimiter: Optional[StrictStr]=None
    encoding_type: Optional[StrictStr]=None
    key_marker: Optional[StrictStr]=None
    max_uploads: Optional[StrictInt]=None
    prefix: Optional[StrictStr]=None
    upload_id_marker: Optional[StrictStr]=None
    expected_bucket_owner: Optional[StrictStr]=None
