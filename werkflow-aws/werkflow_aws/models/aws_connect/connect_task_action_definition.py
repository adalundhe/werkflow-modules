from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_reference import ConnectReference


class ConnectTaskActionDefinition(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ContactFlowId: StrictStr | None = None
    References: dict[StrictStr, ConnectReference] | None = None
