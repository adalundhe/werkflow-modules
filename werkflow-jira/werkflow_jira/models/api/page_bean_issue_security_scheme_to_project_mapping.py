from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .issue_security_scheme_to_project_mapping import IssueSecuritySchemeToProjectMapping


class PageBeanIssueSecuritySchemeToProjectMapping(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[IssueSecuritySchemeToProjectMapping] | None = None
