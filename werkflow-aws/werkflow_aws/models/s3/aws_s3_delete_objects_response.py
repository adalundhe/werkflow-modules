from pydantic import (
    BaseModel,
    StrictStr,
    StrictBool
)

from typing import (
    List,
    Dict,
    Literal,
    Optional
)
from .aws_s3_deleted_object import AWSs3DeletedObject
from .aws_s3_deleted_object_error import AWSs3DeleteObjectError


class AWSs3DeleteObjectsResponse(BaseModel):
    Deleted: List[AWSs3DeletedObject]=[]
    RequestCharged: Optional[
        Literal['requester']
    ]=None
    Errors: List[AWSs3DeleteObjectError]=[]
