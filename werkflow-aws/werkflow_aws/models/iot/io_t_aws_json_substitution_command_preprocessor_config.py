from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTAwsJsonSubstitutionCommandPreprocessorConfig(BaseModel):
    outputFormat: StrictStr | None = None
