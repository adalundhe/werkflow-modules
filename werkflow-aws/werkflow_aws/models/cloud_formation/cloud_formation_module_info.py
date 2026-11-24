from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationModuleInfo(BaseModel):
    TypeHierarchy: StrictStr | None = None
    LogicalIdHierarchy: StrictStr | None = None
