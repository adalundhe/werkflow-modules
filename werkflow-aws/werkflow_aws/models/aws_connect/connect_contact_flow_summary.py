from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectContactFlowSummary(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    ContactFlowType: StrictStr | None = None
    ContactFlowState: StrictStr | None = None
    ContactFlowStatus: StrictStr | None = None
