from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerUiConfig(BaseModel):
    UiTemplateS3Uri: StrictStr | None = None
    HumanTaskUiArn: StrictStr | None = None
