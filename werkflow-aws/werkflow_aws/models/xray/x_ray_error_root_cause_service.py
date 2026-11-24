from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .x_ray_error_root_cause_entity import XRayErrorRootCauseEntity


class XRayErrorRootCauseService(BaseModel):
    Name: StrictStr | None = None
    Names: list[StrictStr] | None = None
    Type: StrictStr | None = None
    AccountId: StrictStr | None = None
    EntityPath: list[XRayErrorRootCauseEntity] | None = None
    Inferred: StrictBool | None = None
