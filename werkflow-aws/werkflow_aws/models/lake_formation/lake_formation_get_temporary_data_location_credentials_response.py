from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_temporary_credentials import LakeFormationTemporaryCredentials


class LakeFormationGetTemporaryDataLocationCredentialsResponse(BaseModel):
    Credentials: LakeFormationTemporaryCredentials | None = None
    AccessibleDataLocations: list[StrictStr] | None = None
    CredentialsScope: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
