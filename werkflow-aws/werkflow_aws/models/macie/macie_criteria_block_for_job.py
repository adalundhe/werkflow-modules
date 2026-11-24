from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from .macie_criteria_for_job import MacieCriteriaForJob


class MacieCriteriaBlockForJob(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    and_: list[MacieCriteriaForJob] | None = Field(default=None, alias='and')
