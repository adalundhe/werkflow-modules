from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCalculatedField(BaseModel):
    DataSetIdentifier: StrictStr | None = None
    TopicIdentifier: StrictStr | None = None
    Name: StrictStr | None = None
    Expression: StrictStr | None = None
