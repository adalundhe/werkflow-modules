from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class CloudFrontTestFunctionRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Name: StrictStr
    IfMatch: StrictStr
    EventObject: StrictBytes | BinaryIO | StrictStr
    Stage: Literal['DEVELOPMENT', 'LIVE'] | None = None
