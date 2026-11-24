from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_image import SageMakerImage


class SageMakerListImagesResponse(BaseModel):
    Images: list[SageMakerImage] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
