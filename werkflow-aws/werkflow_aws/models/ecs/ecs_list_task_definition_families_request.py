from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ECSListTaskDefinitionFamiliesRequest(BaseModel):
    familyPrefix: StrictStr | None = None
    status: Literal['ACTIVE', 'INACTIVE', 'ALL'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
