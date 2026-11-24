from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CreateUpdateRoleRequestBean(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
