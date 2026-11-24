from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncLambdaDataSourceConfig(BaseModel):
    lambdaFunctionArn: StrictStr | None = None
