from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightRegisteredUserQSearchBarEmbeddingConfiguration(BaseModel):
    InitialTopicId: StrictStr | None = None
