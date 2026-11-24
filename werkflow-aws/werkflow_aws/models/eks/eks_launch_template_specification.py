from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSLaunchTemplateSpecification(BaseModel):
    name: StrictStr | None = None
    version: StrictStr | None = None
    id: StrictStr | None = None
