from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .bulk_change_owner_details import BulkChangeOwnerDetails
from .permission_details import PermissionDetails


class BulkEditShareableEntityRequest(BaseModel):
    action: StrictStr | None = None
    changeOwnerDetails: BulkChangeOwnerDetails | None = None
    entityIds: list[StrictInt] | None = None
    extendAdminPermissions: StrictBool | None = None
    permissionDetails: PermissionDetails | None = None
