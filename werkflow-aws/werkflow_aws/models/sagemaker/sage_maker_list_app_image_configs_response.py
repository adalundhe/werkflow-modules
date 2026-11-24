from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_app_image_config_details import SageMakerAppImageConfigDetails


class SageMakerListAppImageConfigsResponse(BaseModel):
    NextToken: StrictStr | None = None
    AppImageConfigs: list[SageMakerAppImageConfigDetails] | None = None
    ResponseMetadata: dict[str, Any] | None = None
