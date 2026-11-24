from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_export_filter import LexExportFilter
from .lex_export_sort_by import LexExportSortBy


class LexListExportsRequest(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    sortBy: LexExportSortBy | None = None
    filters: list[LexExportFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    localeId: StrictStr | None = None
