from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_work_space_application import WorkSpacesWorkSpaceApplication


class WorkSpacesDescribeApplicationsResponse(BaseModel):
    Applications: list[WorkSpacesWorkSpaceApplication] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
