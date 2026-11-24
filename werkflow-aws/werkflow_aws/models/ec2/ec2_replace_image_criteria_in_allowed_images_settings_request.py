from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .ec2_image_criterion_request import EC2ImageCriterionRequest


class EC2ReplaceImageCriteriaInAllowedImagesSettingsRequest(BaseModel):
    ImageCriteria: list[EC2ImageCriterionRequest] | None = None
    DryRun: StrictBool | None = None
