from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAnonymousUserGenerativeQnAEmbeddingConfiguration(BaseModel):
    InitialTopicId: StrictStr
