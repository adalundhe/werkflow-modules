from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexEncryptionSetting(BaseModel):
    kmsKeyArn: StrictStr | None = None
    botLocaleExportPassword: StrictStr | None = None
    associatedTranscriptsPassword: StrictStr | None = None
