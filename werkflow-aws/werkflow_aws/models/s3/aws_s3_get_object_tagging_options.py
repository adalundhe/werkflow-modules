from pydantic import (
    StrictStr
)
from typing import Optional
from werkflow_aws.models.base import AWSBoto3Base


class AWSs3GetObjectTaggingOptions(AWSBoto3Base):
    version_id: Optional[StrictStr]=None
    expected_bucket_owner: Optional[StrictStr]=None