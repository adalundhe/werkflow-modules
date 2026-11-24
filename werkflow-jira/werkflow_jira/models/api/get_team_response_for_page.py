from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GetTeamResponseForPage(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
