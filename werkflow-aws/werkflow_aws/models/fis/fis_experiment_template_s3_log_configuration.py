from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentTemplateS3LogConfiguration(BaseModel):
    bucketName: StrictStr | None = None
    prefix: StrictStr | None = None
