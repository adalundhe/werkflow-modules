from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_rendering_error import SageMakerRenderingError


class SageMakerRenderUiTemplateResponse(BaseModel):
    RenderedContent: StrictStr | None = None
    Errors: list[SageMakerRenderingError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
