from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncLambdaConfig(BaseModel):
    invokeType: StrictStr | None = None
