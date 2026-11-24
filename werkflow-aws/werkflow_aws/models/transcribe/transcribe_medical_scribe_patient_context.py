from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class TranscribeMedicalScribePatientContext(BaseModel):
    Pronouns: Literal['HE_HIM', 'SHE_HER', 'THEY_THEM'] | None = None
