from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class TranscribeMedicalTranscriptionJobSummary(BaseModel):
    MedicalTranscriptionJobName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    CompletionTime: datetime.datetime | StrictStr | None = None
    LanguageCode: StrictStr | None = None
    TranscriptionJobStatus: StrictStr | None = None
    FailureReason: StrictStr | None = None
    OutputLocationType: StrictStr | None = None
    Specialty: StrictStr | None = None
    ContentIdentificationType: StrictStr | None = None
    Type: StrictStr | None = None
