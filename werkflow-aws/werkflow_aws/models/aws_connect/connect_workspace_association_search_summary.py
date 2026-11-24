from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectWorkspaceAssociationSearchSummary(BaseModel):
    WorkspaceId: StrictStr | None = None
    WorkspaceArn: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceName: StrictStr | None = None
