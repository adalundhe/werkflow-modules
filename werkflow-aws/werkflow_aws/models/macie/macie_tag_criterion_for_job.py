from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_tag_criterion_pair_for_job import MacieTagCriterionPairForJob


class MacieTagCriterionForJob(BaseModel):
    comparator: StrictStr | None = None
    tagValues: list[MacieTagCriterionPairForJob] | None = None
