from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class LakeFormationGetTemporaryGlueFunctionCredentialsResponse(BaseModel):
    AccessKeyId: StrictStr | None = None
    SecretAccessKey: StrictStr | None = None
    SessionToken: StrictStr | None = None
    Expiration: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
