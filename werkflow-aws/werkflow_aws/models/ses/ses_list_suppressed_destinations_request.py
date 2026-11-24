from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SESListSuppressedDestinationsRequest(BaseModel):
    TenantName: StrictStr | None = None
    Reasons: list[Literal['BOUNCE', 'COMPLAINT']] | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    NextToken: StrictStr | None = None
    PageSize: StrictInt | None = None
