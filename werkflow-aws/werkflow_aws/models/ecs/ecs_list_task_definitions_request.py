from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ECSListTaskDefinitionsRequest(BaseModel):
    familyPrefix: StrictStr | None = None
    status: Literal['ACTIVE', 'INACTIVE', 'DELETE_IN_PROGRESS'] | None = None
    sort: Literal['ASC', 'DESC'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
