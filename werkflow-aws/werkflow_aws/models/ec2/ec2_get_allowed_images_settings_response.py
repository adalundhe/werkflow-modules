from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_image_criterion import EC2ImageCriterion


class EC2GetAllowedImagesSettingsResponse(BaseModel):
    State: StrictStr | None = None
    ImageCriteria: list[EC2ImageCriterion] | None = None
    ManagedBy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
