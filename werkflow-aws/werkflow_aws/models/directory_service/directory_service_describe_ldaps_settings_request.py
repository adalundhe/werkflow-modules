from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DirectoryServiceDescribeLDAPSSettingsRequest(BaseModel):
    DirectoryId: StrictStr
    Type: Literal['Client'] | None = None
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
