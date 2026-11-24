from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SWFListDomainsRequest(BaseModel):
    registrationStatus: Literal['REGISTERED', 'DEPRECATED']
    nextPageToken: StrictStr | None = None
    maximumPageSize: StrictInt | None = None
    reverseOrder: StrictBool | None = None
