from __future__ import annotations
from pydantic import BaseModel, StrictStr


class UpdateIssueSecuritySchemeRequestBean(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
