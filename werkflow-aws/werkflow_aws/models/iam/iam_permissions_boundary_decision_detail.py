from __future__ import annotations
from pydantic import BaseModel, StrictBool


class IAMPermissionsBoundaryDecisionDetail(BaseModel):
    AllowedByPermissionsBoundary: StrictBool | None = None
