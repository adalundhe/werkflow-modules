from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GlueCrawlsFilter(BaseModel):
    FieldName: Literal['CRAWL_ID', 'STATE', 'START_TIME', 'END_TIME', 'DPU_HOUR'] | None = None
    FilterOperator: Literal['GT', 'GE', 'LT', 'LE', 'EQ', 'NE'] | None = None
    FieldValue: StrictStr | None = None
