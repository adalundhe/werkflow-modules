from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTopicV2DataSetReference(BaseModel):
    DataSetArn: StrictStr | None = None
    DataSetName: StrictStr | None = None
