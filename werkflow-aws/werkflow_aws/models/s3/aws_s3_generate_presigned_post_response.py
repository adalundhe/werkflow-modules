from pydantic import (
    BaseModel,
    StrictStr,
    AnyHttpUrl
)
from typing import Dict


class AWSs3GeneratePresignedPostResponse(BaseModel):
    url: AnyHttpUrl
    fields: Dict[StrictStr, StrictStr]