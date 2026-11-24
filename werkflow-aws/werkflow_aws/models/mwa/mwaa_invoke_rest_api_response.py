from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt
from .mwaa_rest_api_response import MWAARestApiResponse


class MWAAInvokeRestApiResponse(BaseModel):
    RestApiStatusCode: StrictInt | None = None
    RestApiResponse: MWAARestApiResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
