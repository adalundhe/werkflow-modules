from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_lambda_conflict_handler_config import AppSyncLambdaConflictHandlerConfig


class AppSyncSyncConfig(BaseModel):
    conflictHandler: StrictStr | None = None
    conflictDetection: StrictStr | None = None
    lambdaConflictHandlerConfig: AppSyncLambdaConflictHandlerConfig | None = None
