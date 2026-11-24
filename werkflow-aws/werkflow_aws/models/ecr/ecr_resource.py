from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_resource_details import ECRResourceDetails


class ECRResource(BaseModel):
    details: ECRResourceDetails | None = None
    id: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    type: StrictStr | None = None
