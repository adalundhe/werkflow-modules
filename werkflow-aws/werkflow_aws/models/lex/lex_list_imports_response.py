from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_import_summary import LexImportSummary


class LexListImportsResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    importSummaries: list[LexImportSummary] | None = None
    nextToken: StrictStr | None = None
    localeId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
