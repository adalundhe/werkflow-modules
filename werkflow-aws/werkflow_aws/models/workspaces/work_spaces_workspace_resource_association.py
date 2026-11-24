from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .work_spaces_association_state_reason import WorkSpacesAssociationStateReason


class WorkSpacesWorkspaceResourceAssociation(BaseModel):
    AssociatedResourceId: StrictStr | None = None
    AssociatedResourceType: StrictStr | None = None
    Created: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    StateReason: WorkSpacesAssociationStateReason | None = None
    WorkspaceId: StrictStr | None = None
