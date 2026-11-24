from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_import_filter import LexImportFilter
from .lex_import_sort_by import LexImportSortBy


class LexListImportsRequest(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    sortBy: LexImportSortBy | None = None
    filters: list[LexImportFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    localeId: StrictStr | None = None
