from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SSMCredentials(BaseModel):
    AccessKeyId: StrictStr | None = None
    SecretAccessKey: StrictStr | None = None
    SessionToken: StrictStr | None = None
    ExpirationTime: datetime.datetime | StrictStr | None = None
