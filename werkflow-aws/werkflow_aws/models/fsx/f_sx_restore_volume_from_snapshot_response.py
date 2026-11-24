from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_administrative_action import FSxAdministrativeAction


class FSxRestoreVolumeFromSnapshotResponse(BaseModel):
    VolumeId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    AdministrativeActions: list[FSxAdministrativeAction] | None = None
    ResponseMetadata: dict[str, Any] | None = None
