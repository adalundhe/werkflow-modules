from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .textract_encryption_configuration import TextractEncryptionConfiguration


class TextractCreateBlueprintRequest(BaseModel):
    BlueprintName: StrictStr
    Schema: StrictStr
    ClientRequestToken: StrictStr | None = None
    EncryptionConfiguration: TextractEncryptionConfiguration | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
