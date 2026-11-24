from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AWSS3SessionCredentials(BaseModel):
    AccessKeyId: StrictStr | None = None
    SecretAccessKey: StrictStr | None = None
    SessionToken: StrictStr | None = None
    Expiration: datetime.datetime | StrictStr | None = None
