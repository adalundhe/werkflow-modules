from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class AthenaGetSessionEndpointResponse(BaseModel):
    EndpointUrl: StrictStr | None = None
    AuthToken: StrictStr | None = None
    AuthTokenExpirationTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
