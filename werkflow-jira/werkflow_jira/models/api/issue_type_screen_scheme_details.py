from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .issue_type_screen_scheme_mapping import IssueTypeScreenSchemeMapping


class IssueTypeScreenSchemeDetails(BaseModel):
    description: StrictStr | None = None
    issueTypeMappings: list[IssueTypeScreenSchemeMapping] | None = None
    name: StrictStr | None = None
