from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_operating_system import WorkSpacesOperatingSystem


class WorkSpacesCreateWorkspaceImageResponse(BaseModel):
    ImageId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    OperatingSystem: WorkSpacesOperatingSystem | None = None
    State: StrictStr | None = None
    RequiredTenancy: StrictStr | None = None
    Created: datetime.datetime | StrictStr | None = None
    OwnerAccountId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
