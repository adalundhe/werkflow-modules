from __future__ import annotations
from pydantic import BaseModel
from .q_business_attribute_filter import QBusinessAttributeFilter


class QBusinessActionFilterConfiguration(BaseModel):
    documentAttributeFilter: QBusinessAttributeFilter | None = None
