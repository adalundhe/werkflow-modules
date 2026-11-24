from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_image_version import SageMakerImageVersion


class SageMakerListImageVersionsResponse(BaseModel):
    ImageVersions: list[SageMakerImageVersion] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
