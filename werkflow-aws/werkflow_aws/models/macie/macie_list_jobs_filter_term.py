from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MacieListJobsFilterTerm(BaseModel):
    comparator: Literal['EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'CONTAINS', 'STARTS_WITH'] | None = None
    key: Literal['jobType', 'jobStatus', 'createdAt', 'name'] | None = None
    values: list[StrictStr] | None = None
