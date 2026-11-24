from __future__ import annotations
from pydantic import BaseModel
from .lex_test_set_discrepancy_report_bot_alias_target import LexTestSetDiscrepancyReportBotAliasTarget


class LexTestSetDiscrepancyReportResourceTarget(BaseModel):
    botAliasTarget: LexTestSetDiscrepancyReportBotAliasTarget | None = None
