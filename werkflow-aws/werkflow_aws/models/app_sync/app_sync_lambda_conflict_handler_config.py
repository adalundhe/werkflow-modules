from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncLambdaConflictHandlerConfig(BaseModel):
    lambdaConflictHandlerArn: StrictStr | None = None
