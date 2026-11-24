from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .emr_persistent_app_ui import EMRPersistentAppUI


class EMRDescribePersistentAppUIResponse(BaseModel):
    PersistentAppUI: EMRPersistentAppUI | None = None
    ResponseMetadata: dict[str, Any] | None = None
