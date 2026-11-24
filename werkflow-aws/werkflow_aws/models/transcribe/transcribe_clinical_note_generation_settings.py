from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeClinicalNoteGenerationSettings(BaseModel):
    NoteTemplate: StrictStr | None = None
