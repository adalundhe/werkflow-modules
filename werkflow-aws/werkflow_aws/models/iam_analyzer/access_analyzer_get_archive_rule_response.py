from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .access_analyzer_archive_rule_summary import AccessAnalyzerArchiveRuleSummary


class AccessAnalyzerGetArchiveRuleResponse(BaseModel):
    archiveRule: AccessAnalyzerArchiveRuleSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
