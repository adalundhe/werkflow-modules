from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .mwaa_document import MWAADocument
from .mwaa_rest_api_request_body import MWAARestApiRequestBody


class MWAAInvokeRestApiRequest(BaseModel):
    Name: StrictStr
    Path: StrictStr
    Method: Literal['GET', 'PUT', 'POST', 'PATCH', 'DELETE']
    QueryParameters: MWAADocument | None = None
    Body: MWAARestApiRequestBody | None = None
