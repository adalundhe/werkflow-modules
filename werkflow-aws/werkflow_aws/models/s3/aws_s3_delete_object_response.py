from pydantic import BaseModel, StrictStr, StrictBool
from typing import Literal, Optional


class AWSS3DeleteObjectResponse(BaseModel):
    DeleteMarker: StrictBool
    VersionId: StrictStr
    RequestCharged: Optional[
        Literal['requester']
    ]=None