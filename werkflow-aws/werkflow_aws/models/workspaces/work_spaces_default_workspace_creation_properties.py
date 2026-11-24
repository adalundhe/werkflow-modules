from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class WorkSpacesDefaultWorkspaceCreationProperties(BaseModel):
    EnableInternetAccess: StrictBool | None = None
    DefaultOu: StrictStr | None = None
    CustomSecurityGroupId: StrictStr | None = None
    UserEnabledAsLocalAdministrator: StrictBool | None = None
    EnableMaintenanceMode: StrictBool | None = None
    InstanceIamRoleArn: StrictStr | None = None
