from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class TranscribeMedicalScribeJobSummary(BaseModel):
    MedicalScribeJobName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    CompletionTime: datetime.datetime | StrictStr | None = None
    LanguageCode: StrictStr | None = None
    MedicalScribeJobStatus: StrictStr | None = None
    FailureReason: StrictStr | None = None
