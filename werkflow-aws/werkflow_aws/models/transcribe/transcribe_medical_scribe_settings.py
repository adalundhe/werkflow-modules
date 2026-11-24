from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .transcribe_clinical_note_generation_settings import TranscribeClinicalNoteGenerationSettings


class TranscribeMedicalScribeSettings(BaseModel):
    ShowSpeakerLabels: StrictBool | None = None
    MaxSpeakerLabels: StrictInt | None = None
    ChannelIdentification: StrictBool | None = None
    VocabularyName: StrictStr | None = None
    VocabularyFilterName: StrictStr | None = None
    VocabularyFilterMethod: StrictStr | None = None
    ClinicalNoteGenerationSettings: TranscribeClinicalNoteGenerationSettings | None = None
