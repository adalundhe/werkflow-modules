from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsDescribePolicyRequest(BaseModel):
    PolicyId: StrictStr | None = None
