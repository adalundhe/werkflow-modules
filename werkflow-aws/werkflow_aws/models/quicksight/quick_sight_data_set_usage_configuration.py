from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightDataSetUsageConfiguration(BaseModel):
    DisableUseAsDirectQuerySource: StrictBool | None = None
    DisableUseAsImportedSource: StrictBool | None = None
