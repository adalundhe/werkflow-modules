from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_extension_summary import SageMakerExtensionSummary


class SageMakerListClusterExtensionsResponse(BaseModel):
    Extensions: list[SageMakerExtensionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
