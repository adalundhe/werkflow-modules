from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .translate_encryption_key import TranslateEncryptionKey
from .translate_tag import TranslateTag
from .translate_terminology_data import TranslateTerminologyData


class TranslateImportTerminologyRequest(BaseModel):
    Name: StrictStr
    MergeStrategy: Literal['OVERWRITE']
    TerminologyData: TranslateTerminologyData
    Description: StrictStr | None = None
    EncryptionKey: TranslateEncryptionKey | None = None
    Tags: list[TranslateTag] | None = None
