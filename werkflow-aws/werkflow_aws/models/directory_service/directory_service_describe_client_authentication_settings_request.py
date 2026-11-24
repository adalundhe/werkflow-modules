from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DirectoryServiceDescribeClientAuthenticationSettingsRequest(BaseModel):
    DirectoryId: StrictStr
    Type: Literal['SmartCard', 'SmartCardOrPassword'] | None = None
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
