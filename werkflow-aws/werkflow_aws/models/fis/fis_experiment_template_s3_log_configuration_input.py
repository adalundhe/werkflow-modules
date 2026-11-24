from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentTemplateS3LogConfigurationInput(BaseModel):
    bucketName: StrictStr
    prefix: StrictStr | None = None
