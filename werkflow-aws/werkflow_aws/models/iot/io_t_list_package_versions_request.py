from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListPackageVersionsRequest(BaseModel):
    packageName: StrictStr
    status: Literal['DRAFT', 'PUBLISHED', 'DEPRECATED'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
