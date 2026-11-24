from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightColumnIdentifier(BaseModel):
    DataSetIdentifier: StrictStr | None = None
    TopicIdentifier: StrictStr | None = None
    ColumnName: StrictStr | None = None
