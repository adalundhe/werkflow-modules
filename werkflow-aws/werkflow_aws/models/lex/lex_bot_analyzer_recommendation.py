from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_issue_location import LexIssueLocation


class LexBotAnalyzerRecommendation(BaseModel):
    issueLocation: LexIssueLocation | None = None
    priority: StrictStr | None = None
    issueDescription: StrictStr | None = None
    proposedFix: StrictStr | None = None
