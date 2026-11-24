from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .issue_field_option_scope_bean import IssueFieldOptionScopeBean


class IssueFieldOptionConfiguration(BaseModel):
    attributes: list[StrictStr] | None = None
    scope: IssueFieldOptionScopeBean | None = None
