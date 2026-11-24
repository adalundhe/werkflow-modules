from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDescribeEventCategoriesRequest(BaseModel):
    SourceType: StrictStr | None = None
