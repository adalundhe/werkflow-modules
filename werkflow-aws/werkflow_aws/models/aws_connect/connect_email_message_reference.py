from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEmailMessageReference(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
