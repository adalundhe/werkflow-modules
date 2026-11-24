from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_extension_version_summary import SageMakerExtensionVersionSummary


class SageMakerListClusterExtensionVersionsResponse(BaseModel):
    ExtensionVersions: list[SageMakerExtensionVersionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
