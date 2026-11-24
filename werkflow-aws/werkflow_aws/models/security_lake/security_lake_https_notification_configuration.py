from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SecurityLakeHttpsNotificationConfiguration(BaseModel):
    endpoint: StrictStr
    targetRoleArn: StrictStr
    authorizationApiKeyName: StrictStr | None = None
    authorizationApiKeyValue: StrictStr | None = None
    httpMethod: Literal['POST', 'PUT'] | None = None
