from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class KendraContentSourceConfiguration(BaseModel):
    DataSourceIds: list[StrictStr] | None = None
    FaqIds: list[StrictStr] | None = None
    DirectPutContent: StrictBool | None = None
