from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_thin_client_environment_summary import WorkSpacesThinClientEnvironmentSummary


class WorkSpacesThinClientUpdateEnvironmentResponse(BaseModel):
    environment: WorkSpacesThinClientEnvironmentSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
