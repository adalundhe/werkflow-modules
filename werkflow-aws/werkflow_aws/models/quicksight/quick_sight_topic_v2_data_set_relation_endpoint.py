from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTopicV2DataSetRelationEndpoint(BaseModel):
    DataSetArn: StrictStr | None = None
    ColumnNames: list[StrictStr] | None = None
