from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSExpressGatewayServiceAwsLogsConfiguration(BaseModel):
    logGroup: StrictStr | None = None
    logStreamPrefix: StrictStr | None = None
