from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_criterion_additional_properties import MacieCriterionAdditionalProperties


class MacieFindingCriteria(BaseModel):
    criterion: dict[StrictStr, MacieCriterionAdditionalProperties] | None = None
