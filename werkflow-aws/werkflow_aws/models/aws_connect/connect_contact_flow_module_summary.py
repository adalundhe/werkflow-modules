from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectContactFlowModuleSummary(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    State: StrictStr | None = None
