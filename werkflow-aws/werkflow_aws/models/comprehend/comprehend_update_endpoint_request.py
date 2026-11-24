from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ComprehendUpdateEndpointRequest(BaseModel):
    EndpointArn: StrictStr
    DesiredModelArn: StrictStr | None = None
    DesiredInferenceUnits: StrictInt | None = None
    DesiredDataAccessRoleArn: StrictStr | None = None
    FlywheelArn: StrictStr | None = None
