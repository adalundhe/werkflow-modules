from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectHoursOfOperationsIdentifier(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
