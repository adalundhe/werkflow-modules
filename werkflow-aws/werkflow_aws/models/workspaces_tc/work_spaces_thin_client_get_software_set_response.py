from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_thin_client_software_set import WorkSpacesThinClientSoftwareSet


class WorkSpacesThinClientGetSoftwareSetResponse(BaseModel):
    softwareSet: WorkSpacesThinClientSoftwareSet | None = None
    ResponseMetadata: dict[str, Any] | None = None
