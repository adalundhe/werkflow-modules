from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictStr


class APIGatewayImportApiKeysRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    body: StrictBytes | BinaryIO | StrictStr
    format: Literal['csv']
    failOnWarnings: StrictBool | None = None
