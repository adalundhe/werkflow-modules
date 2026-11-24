from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .emr_credentials import EMRCredentials


class EMRGetClusterSessionCredentialsResponse(BaseModel):
    Credentials: EMRCredentials | None = None
    ExpiresAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
