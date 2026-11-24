from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ProjectEmailAddress(BaseModel):
    emailAddress: StrictStr | None = None
    emailAddressStatus: list[StrictStr] | None = None
