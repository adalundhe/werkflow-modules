from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_thin_client_environment_summary import WorkSpacesThinClientEnvironmentSummary


class WorkSpacesThinClientListEnvironmentsResponse(BaseModel):
    environments: list[WorkSpacesThinClientEnvironmentSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
