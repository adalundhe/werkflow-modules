from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class CloudFrontTestConnectionFunctionRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Id: StrictStr
    IfMatch: StrictStr
    ConnectionObject: StrictBytes | BinaryIO | StrictStr
    Stage: Literal['DEVELOPMENT', 'LIVE'] | None = None
