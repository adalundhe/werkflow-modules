from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .textract_encryption_configuration import TextractEncryptionConfiguration


class TextractUpdateBlueprintRequest(BaseModel):
    BlueprintArn: StrictStr
    Schema: StrictStr | None = None
    EncryptionConfiguration: TextractEncryptionConfiguration | None = None
