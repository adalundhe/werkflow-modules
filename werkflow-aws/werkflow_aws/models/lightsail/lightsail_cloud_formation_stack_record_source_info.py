from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailCloudFormationStackRecordSourceInfo(BaseModel):
    resourceType: StrictStr | None = None
    name: StrictStr | None = None
    arn: StrictStr | None = None
