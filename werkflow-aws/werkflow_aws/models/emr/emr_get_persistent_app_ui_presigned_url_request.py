from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EMRGetPersistentAppUIPresignedURLRequest(BaseModel):
    PersistentAppUIId: StrictStr
    PersistentAppUIType: Literal['SHS', 'TEZ', 'YTS'] | None = None
    ApplicationId: StrictStr | None = None
    AuthProxyCall: StrictBool | None = None
    ExecutionRoleArn: StrictStr | None = None
