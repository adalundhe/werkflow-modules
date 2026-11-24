from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ECSDeregisterContainerInstanceRequest(BaseModel):
    containerInstance: StrictStr
    cluster: StrictStr | None = None
    force: StrictBool | None = None
