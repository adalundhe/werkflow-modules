from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_thin_client_environment import WorkSpacesThinClientEnvironment


class WorkSpacesThinClientGetEnvironmentResponse(BaseModel):
    environment: WorkSpacesThinClientEnvironment | None = None
    ResponseMetadata: dict[str, Any] | None = None
