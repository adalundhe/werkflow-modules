from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictStr


class APIGatewayPutRestApiRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    restApiId: StrictStr
    body: StrictBytes | BinaryIO | StrictStr
    mode: Literal['merge', 'overwrite'] | None = None
    failOnWarnings: StrictBool | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
