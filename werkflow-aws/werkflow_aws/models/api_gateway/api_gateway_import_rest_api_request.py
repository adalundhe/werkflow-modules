from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBool, StrictBytes, StrictStr


class APIGatewayImportRestApiRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    body: StrictBytes | BinaryIO | StrictStr
    failOnWarnings: StrictBool | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
