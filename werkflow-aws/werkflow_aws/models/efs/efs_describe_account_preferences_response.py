from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .efs_resource_id_preference import EFSResourceIdPreference


class EFSDescribeAccountPreferencesResponse(BaseModel):
    ResourceIdPreference: EFSResourceIdPreference | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
