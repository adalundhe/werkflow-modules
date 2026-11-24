from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneCustomAccountPoolHandler(BaseModel):
    lambdaFunctionArn: StrictStr | None = None
    lambdaExecutionRoleArn: StrictStr | None = None
