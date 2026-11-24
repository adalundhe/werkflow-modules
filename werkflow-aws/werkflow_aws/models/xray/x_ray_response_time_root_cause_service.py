from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .x_ray_response_time_root_cause_entity import XRayResponseTimeRootCauseEntity


class XRayResponseTimeRootCauseService(BaseModel):
    Name: StrictStr | None = None
    Names: list[StrictStr] | None = None
    Type: StrictStr | None = None
    AccountId: StrictStr | None = None
    EntityPath: list[XRayResponseTimeRootCauseEntity] | None = None
    Inferred: StrictBool | None = None
