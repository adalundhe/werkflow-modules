from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SageMakerChannelSpecification(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    IsRequired: StrictBool | None = None
    SupportedContentTypes: list[StrictStr] | None = None
    SupportedCompressionTypes: list[StrictStr] | None = None
    SupportedInputModes: list[StrictStr] | None = None
