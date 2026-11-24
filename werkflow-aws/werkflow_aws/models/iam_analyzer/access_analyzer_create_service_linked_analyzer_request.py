from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .access_analyzer_analyzer_configuration import AccessAnalyzerAnalyzerConfiguration
from .access_analyzer_inline_archive_rule import AccessAnalyzerInlineArchiveRule


class AccessAnalyzerCreateServiceLinkedAnalyzerRequest(BaseModel):
    type: Literal['ACCOUNT', 'ORGANIZATION', 'ACCOUNT_UNUSED_ACCESS', 'ORGANIZATION_UNUSED_ACCESS', 'ACCOUNT_INTERNAL_ACCESS', 'ORGANIZATION_INTERNAL_ACCESS']
    archiveRules: list[AccessAnalyzerInlineArchiveRule] | None = None
    clientToken: StrictStr | None = None
    configuration: AccessAnalyzerAnalyzerConfiguration | None = None
