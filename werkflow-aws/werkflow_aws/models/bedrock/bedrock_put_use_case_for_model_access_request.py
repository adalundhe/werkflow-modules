from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class BedrockPutUseCaseForModelAccessRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    formData: StrictBytes | BinaryIO | StrictStr
