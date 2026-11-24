from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTopicV2Summary(BaseModel):
    Arn: StrictStr | None = None
    TopicId: StrictStr | None = None
    Name: StrictStr | None = None
