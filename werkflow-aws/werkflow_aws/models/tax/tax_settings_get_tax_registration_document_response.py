from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class TaxSettingsGetTaxRegistrationDocumentResponse(BaseModel):
    destinationFilePath: StrictStr | None = None
    presignedS3Url: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
