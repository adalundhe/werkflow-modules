from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerIamRoleConfiguration(BaseModel):
    trustPolicy: StrictStr | None = None
