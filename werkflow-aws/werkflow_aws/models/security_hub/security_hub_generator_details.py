from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubGeneratorDetails(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Labels: list[StrictStr] | None = None
