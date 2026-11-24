from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightRegisteredUserGenerativeQnAEmbeddingConfiguration(BaseModel):
    InitialTopicId: StrictStr | None = None
