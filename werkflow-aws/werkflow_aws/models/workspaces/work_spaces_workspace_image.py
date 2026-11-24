from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .work_spaces_error_details import WorkSpacesErrorDetails
from .work_spaces_operating_system import WorkSpacesOperatingSystem
from .work_spaces_update_result import WorkSpacesUpdateResult


class WorkSpacesWorkspaceImage(BaseModel):
    ImageId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    OperatingSystem: WorkSpacesOperatingSystem | None = None
    State: StrictStr | None = None
    RequiredTenancy: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    Created: datetime.datetime | StrictStr | None = None
    OwnerAccountId: StrictStr | None = None
    Updates: WorkSpacesUpdateResult | None = None
    ErrorDetails: list[WorkSpacesErrorDetails] | None = None
