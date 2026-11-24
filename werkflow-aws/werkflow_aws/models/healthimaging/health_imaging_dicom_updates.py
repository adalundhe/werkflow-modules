from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class HealthImagingDICOMUpdates(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    removableAttributes: StrictBytes | BinaryIO | StrictStr | None = None
    updatableAttributes: StrictBytes | BinaryIO | StrictStr | None = None
