from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes


class APIGatewayV2ExportApiResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    body: StrictBytes | Any | None = None
    ResponseMetadata: dict[str, Any] | None = None
