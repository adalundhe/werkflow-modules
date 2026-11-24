from __future__ import annotations
from pydantic import BaseModel
from .macie_list_jobs_filter_term import MacieListJobsFilterTerm


class MacieListJobsFilterCriteria(BaseModel):
    excludes: list[MacieListJobsFilterTerm] | None = None
    includes: list[MacieListJobsFilterTerm] | None = None
