from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .efs_resource_id_preference import EFSResourceIdPreference


class EFSPutAccountPreferencesResponse(BaseModel):
    ResourceIdPreference: EFSResourceIdPreference | None = None
    ResponseMetadata: dict[str, Any] | None = None
