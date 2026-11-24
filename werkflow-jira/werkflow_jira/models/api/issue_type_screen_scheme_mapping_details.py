from __future__ import annotations
from pydantic import BaseModel
from .issue_type_screen_scheme_mapping import IssueTypeScreenSchemeMapping


class IssueTypeScreenSchemeMappingDetails(BaseModel):
    issueTypeMappings: list[IssueTypeScreenSchemeMapping] | None = None
