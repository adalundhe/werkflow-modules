from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_aws_iam_config import AppSyncAwsIamConfig


class AppSyncAuthorizationConfig(BaseModel):
    authorizationType: StrictStr | None = None
    awsIamConfig: AppSyncAwsIamConfig | None = None
