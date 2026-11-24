from __future__ import annotations
from pydantic import BaseModel
from .macie_criteria_block_for_job import MacieCriteriaBlockForJob


class MacieS3BucketCriteriaForJob(BaseModel):
    excludes: MacieCriteriaBlockForJob | None = None
    includes: MacieCriteriaBlockForJob | None = None
