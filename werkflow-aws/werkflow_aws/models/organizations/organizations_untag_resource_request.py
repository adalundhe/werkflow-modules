from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsUntagResourceRequest(BaseModel):
    ResourceId: StrictStr | None = None
    TagKeys: list[StrictStr] | None = None
