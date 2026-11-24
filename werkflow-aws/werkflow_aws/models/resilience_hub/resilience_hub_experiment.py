from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubExperiment(BaseModel):
    experimentArn: StrictStr | None = None
    experimentTemplateId: StrictStr | None = None
