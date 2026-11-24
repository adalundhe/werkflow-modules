from pydantic import (
    BaseModel,
    StrictStr
)
from typing import Dict, Any


class AWSs3PutObjectTaggingResponse(BaseModel):
    VersionId: StrictStr | None = None
    ResponseMetadata: Dict[StrictStr, Any] | None = None
