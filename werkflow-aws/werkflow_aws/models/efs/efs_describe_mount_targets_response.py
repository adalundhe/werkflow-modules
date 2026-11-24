from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .efs_mount_target_description import EFSMountTargetDescription


class EFSDescribeMountTargetsResponse(BaseModel):
    Marker: StrictStr | None = None
    MountTargets: list[EFSMountTargetDescription] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
