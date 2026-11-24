from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerDeployedImageModel(BaseModel):
    SpecifiedImage: StrictStr | None = None
    ResolvedImage: StrictStr | None = None
    ResolutionTime: datetime.datetime | StrictStr | None = None
