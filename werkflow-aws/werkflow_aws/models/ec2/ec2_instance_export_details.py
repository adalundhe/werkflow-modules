from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2InstanceExportDetails(BaseModel):
    InstanceId: StrictStr | None = None
    TargetEnvironment: StrictStr | None = None
