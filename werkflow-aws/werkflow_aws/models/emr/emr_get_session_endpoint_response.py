from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .emr_credentials import EMRCredentials


class EMRGetSessionEndpointResponse(BaseModel):
    Endpoint: StrictStr | None = None
    AuthToken: StrictStr | None = None
    AuthTokenExpirationTime: datetime.datetime | StrictStr | None = None
    Credentials: EMRCredentials | None = None
    ResponseMetadata: dict[str, Any] | None = None
