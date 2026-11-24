from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .access_analyzer_archive_rule_summary import AccessAnalyzerArchiveRuleSummary


class AccessAnalyzerListArchiveRulesResponse(BaseModel):
    archiveRules: list[AccessAnalyzerArchiveRuleSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
