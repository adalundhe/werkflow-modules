from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .translate_encryption_key import TranslateEncryptionKey


class TranslateOutputDataConfig(BaseModel):
    S3Uri: StrictStr | None = None
    EncryptionKey: TranslateEncryptionKey | None = None
