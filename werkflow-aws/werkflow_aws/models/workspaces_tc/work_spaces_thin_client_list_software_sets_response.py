from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_thin_client_software_set_summary import WorkSpacesThinClientSoftwareSetSummary


class WorkSpacesThinClientListSoftwareSetsResponse(BaseModel):
    softwareSets: list[WorkSpacesThinClientSoftwareSetSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
