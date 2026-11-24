from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr
from .security_scheme_level_bean import SecuritySchemeLevelBean


class CreateIssueSecuritySchemeDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    description: StrictStr | None = None
    levels: list[SecuritySchemeLevelBean] | None = None
    name: StrictStr | None = None
