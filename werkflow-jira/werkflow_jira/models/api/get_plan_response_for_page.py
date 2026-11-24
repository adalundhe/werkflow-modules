from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .get_issue_source_response import GetIssueSourceResponse


class GetPlanResponseForPage(BaseModel):
    id: StrictStr | None = None
    issueSources: list[GetIssueSourceResponse] | None = None
    name: StrictStr | None = None
    scenarioId: StrictStr | None = None
    status: StrictStr | None = None
