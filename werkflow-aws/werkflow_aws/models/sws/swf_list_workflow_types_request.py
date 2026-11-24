from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SWFListWorkflowTypesRequest(BaseModel):
    domain: StrictStr
    registrationStatus: Literal['REGISTERED', 'DEPRECATED']
    name: StrictStr | None = None
    nextPageToken: StrictStr | None = None
    maximumPageSize: StrictInt | None = None
    reverseOrder: StrictBool | None = None
