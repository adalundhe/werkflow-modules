from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectViewSummary(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Status: StrictStr | None = None
    Description: StrictStr | None = None
