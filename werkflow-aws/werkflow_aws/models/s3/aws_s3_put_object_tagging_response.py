from pydantic import (
    BaseModel,
    StrictStr
)
from typing import Dict, Any


class AWSs3PutObjectTaggingResponse(BaseModel):
    VersionId: StrictStr
    ResponseMetadata: Dict[
        StrictStr,
        Any
    ]