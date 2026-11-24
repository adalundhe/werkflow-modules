from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectFlowAssociationSummary(BaseModel):
    ResourceId: StrictStr | None = None
    FlowId: StrictStr | None = None
    ResourceType: StrictStr | None = None
