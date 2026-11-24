from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_source_processing_properties import GlueSourceProcessingProperties
from .glue_target_processing_properties import GlueTargetProcessingProperties


class GlueCreateIntegrationResourcePropertyResponse(BaseModel):
    ResourceArn: StrictStr | None = None
    ResourcePropertyArn: StrictStr | None = None
    SourceProcessingProperties: GlueSourceProcessingProperties | None = None
    TargetProcessingProperties: GlueTargetProcessingProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
