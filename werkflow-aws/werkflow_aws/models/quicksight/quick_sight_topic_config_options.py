from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightTopicConfigOptions(BaseModel):
    QBusinessInsightsEnabled: StrictBool | None = None
