from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class RedshiftGetClusterCredentialsWithIAMResponse(BaseModel):
    DbUser: StrictStr | None = None
    DbPassword: StrictStr | None = None
    Expiration: datetime.datetime | StrictStr | None = None
    NextRefreshTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
