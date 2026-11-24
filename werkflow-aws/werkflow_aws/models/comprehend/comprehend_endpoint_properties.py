from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ComprehendEndpointProperties(BaseModel):
    EndpointArn: StrictStr | None = None
    Status: StrictStr | None = None
    Message: StrictStr | None = None
    ModelArn: StrictStr | None = None
    DesiredModelArn: StrictStr | None = None
    DesiredInferenceUnits: StrictInt | None = None
    CurrentInferenceUnits: StrictInt | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    DataAccessRoleArn: StrictStr | None = None
    DesiredDataAccessRoleArn: StrictStr | None = None
    FlywheelArn: StrictStr | None = None
