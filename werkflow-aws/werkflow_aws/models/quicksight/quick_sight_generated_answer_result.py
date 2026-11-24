from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGeneratedAnswerResult(BaseModel):
    QuestionText: StrictStr | None = None
    AnswerStatus: StrictStr | None = None
    TopicId: StrictStr | None = None
    TopicName: StrictStr | None = None
    Restatement: StrictStr | None = None
    QuestionId: StrictStr | None = None
    AnswerId: StrictStr | None = None
    QuestionUrl: StrictStr | None = None
