from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueConnectorDataTarget(BaseModel):
    Name: StrictStr | None = None
    ConnectionType: StrictStr | None = None
    Data: dict[StrictStr, StrictStr] | None = None
    Inputs: list[StrictStr] | None = None
