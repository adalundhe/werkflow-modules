from __future__ import annotations
from pydantic import BaseModel
from .q_business_eligible_data_source import QBusinessEligibleDataSource


class QBusinessContentRetrievalRule(BaseModel):
    eligibleDataSources: list[QBusinessEligibleDataSource] | None = None
