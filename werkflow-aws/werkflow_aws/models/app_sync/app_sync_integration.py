from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_lambda_config import AppSyncLambdaConfig


class AppSyncIntegration(BaseModel):
    dataSourceName: StrictStr | None = None
    lambdaConfig: AppSyncLambdaConfig | None = None
