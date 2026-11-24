from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .textract_pii_entities_configuration import TextractPIIEntitiesConfiguration


class TextractSensitiveDataConfiguration(BaseModel):
    DetectionMode: StrictStr | None = None
    PiiEntitiesConfiguration: TextractPIIEntitiesConfiguration | None = None
