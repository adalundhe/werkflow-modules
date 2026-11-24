from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SESListEmailIdentitiesRequest(BaseModel):
    Filter: dict[Literal['IDENTITY_NAME_CONTAINS', 'IDENTITY_TYPE', 'VERIFICATION_STATUS'], StrictStr] | None = None
    NextToken: StrictStr | None = None
    PageSize: StrictInt | None = None
