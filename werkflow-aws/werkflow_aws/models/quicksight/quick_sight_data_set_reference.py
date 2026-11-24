from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDataSetReference(BaseModel):
    DataSetPlaceholder: StrictStr
    DataSetArn: StrictStr
