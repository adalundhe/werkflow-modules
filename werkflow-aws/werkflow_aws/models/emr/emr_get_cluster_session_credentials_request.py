from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRGetClusterSessionCredentialsRequest(BaseModel):
    ClusterId: StrictStr
    ExecutionRoleArn: StrictStr | None = None
