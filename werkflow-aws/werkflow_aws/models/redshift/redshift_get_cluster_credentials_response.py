from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class RedshiftGetClusterCredentialsResponse(BaseModel):
    DbUser: StrictStr | None = None
    DbPassword: StrictStr | None = None
    Expiration: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
