from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_export_summary import LexExportSummary


class LexListExportsResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    exportSummaries: list[LexExportSummary] | None = None
    nextToken: StrictStr | None = None
    localeId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
