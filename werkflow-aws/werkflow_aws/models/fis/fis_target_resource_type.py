from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fis_target_resource_type_parameter import FISTargetResourceTypeParameter


class FISTargetResourceType(BaseModel):
    resourceType: StrictStr | None = None
    description: StrictStr | None = None
    parameters: dict[StrictStr, FISTargetResourceTypeParameter] | None = None
