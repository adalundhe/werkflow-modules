from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectContactDetails(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
