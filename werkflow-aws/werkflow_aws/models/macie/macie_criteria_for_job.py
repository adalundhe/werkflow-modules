from __future__ import annotations
from pydantic import BaseModel
from .macie_simple_criterion_for_job import MacieSimpleCriterionForJob
from .macie_tag_criterion_for_job import MacieTagCriterionForJob


class MacieCriteriaForJob(BaseModel):
    simpleCriterion: MacieSimpleCriterionForJob | None = None
    tagCriterion: MacieTagCriterionForJob | None = None
