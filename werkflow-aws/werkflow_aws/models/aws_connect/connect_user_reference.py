from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUserReference(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
