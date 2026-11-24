from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CognitoIDPClientSecretDescriptorType(BaseModel):
    ClientSecretId: StrictStr | None = None
    ClientSecretValue: StrictStr | None = None
    ClientSecretCreateDate: datetime.datetime | StrictStr | None = None
