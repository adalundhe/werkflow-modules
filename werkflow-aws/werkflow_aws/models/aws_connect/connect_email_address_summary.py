from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectEmailAddressSummary(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    IsDefaultOutboundEmail: StrictBool | None = None
