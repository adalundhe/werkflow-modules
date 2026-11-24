from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class TaxSettingsExemptionCertificate(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    documentName: StrictStr
    documentFile: StrictBytes | BinaryIO | StrictStr
