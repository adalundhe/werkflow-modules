from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GetProjectsWithFieldSchemesResponse(BaseModel):
    projectId: StrictInt | None = None
    schemeId: StrictInt | None = None
