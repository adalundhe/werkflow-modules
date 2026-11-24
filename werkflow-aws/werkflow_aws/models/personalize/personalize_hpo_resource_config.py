from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeHPOResourceConfig(BaseModel):
    maxNumberOfTrainingJobs: StrictStr | None = None
    maxParallelTrainingJobs: StrictStr | None = None
