from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_selfservice_permissions import WorkSpacesSelfservicePermissions


class WorkSpacesModifySelfservicePermissionsRequest(BaseModel):
    ResourceId: StrictStr
    SelfservicePermissions: WorkSpacesSelfservicePermissions
