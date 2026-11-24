from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_filter_model import RDSFilterModel


class RDSDescribeEventCategoriesRequest(BaseModel):
    SourceType: StrictStr | None = None
    Filters: list[RDSFilterModel] | None = None
