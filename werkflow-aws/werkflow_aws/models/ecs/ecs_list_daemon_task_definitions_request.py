from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ECSListDaemonTaskDefinitionsRequest(BaseModel):
    familyPrefix: StrictStr | None = None
    family: StrictStr | None = None
    revision: Literal['LAST_REGISTERED'] | None = None
    status: Literal['ACTIVE', 'DELETE_IN_PROGRESS', 'ALL'] | None = None
    sort: Literal['ASC', 'DESC'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
