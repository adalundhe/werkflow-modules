from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .comprehend_tag import ComprehendTag


class ComprehendCreateEndpointRequest(BaseModel):
    EndpointName: StrictStr
    DesiredInferenceUnits: StrictInt
    ModelArn: StrictStr | None = None
    ClientRequestToken: StrictStr | None = None
    Tags: list[ComprehendTag] | None = None
    DataAccessRoleArn: StrictStr | None = None
    FlywheelArn: StrictStr | None = None
