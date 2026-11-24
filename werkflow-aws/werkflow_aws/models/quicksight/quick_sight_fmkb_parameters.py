from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightFMKBParameters(BaseModel):
    KnowledgeBaseArn: StrictStr | None = None
    LinkedDataSourceIds: list[StrictStr] | None = None
