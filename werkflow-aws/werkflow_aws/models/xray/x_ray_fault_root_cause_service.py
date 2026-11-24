from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .x_ray_fault_root_cause_entity import XRayFaultRootCauseEntity


class XRayFaultRootCauseService(BaseModel):
    Name: StrictStr | None = None
    Names: list[StrictStr] | None = None
    Type: StrictStr | None = None
    AccountId: StrictStr | None = None
    EntityPath: list[XRayFaultRootCauseEntity] | None = None
    Inferred: StrictBool | None = None
