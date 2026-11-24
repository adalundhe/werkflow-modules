from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class BedrockImportedModelSummary(BaseModel):
    modelArn: StrictStr | None = None
    modelName: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    instructSupported: StrictBool | None = None
    modelArchitecture: StrictStr | None = None
