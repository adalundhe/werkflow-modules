import datetime
from pydantic import (
    StrictStr,
    StrictInt
)

from typing import Optional, Literal, List
from werkflow_aws.models.base import AWSBoto3Base


class AWSs3ListObjectVersionsOptions(AWSBoto3Base):
    delimiter: Optional[StrictStr]=None,
    encodying_type: Optional[Literal['url']]=None,
    key_marker: Optional[StrictStr]=None,
    max_keys: Optional[StrictInt]=None,
    prefix: Optional[StrictStr]=None,
    version_id_marker: Optional[StrictStr]=None,
    expected_bucket_owner: Optional[StrictStr]=None,
    request_payer: Optional[Literal['requester']]=None,
    optional_object_attributes: Optional[List[StrictStr]]=None

