from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .translate_encryption_key import TranslateEncryptionKey
from .translate_parallel_data_config import TranslateParallelDataConfig
from .translate_tag import TranslateTag


class TranslateCreateParallelDataRequest(BaseModel):
    Name: StrictStr
    ParallelDataConfig: TranslateParallelDataConfig
    ClientToken: StrictStr
    Description: StrictStr | None = None
    EncryptionKey: TranslateEncryptionKey | None = None
    Tags: list[TranslateTag] | None = None
