from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerSnsTopicConfiguration(BaseModel):
    topicPolicy: StrictStr | None = None
