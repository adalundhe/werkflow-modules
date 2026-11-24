from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_source_processing_properties import GlueSourceProcessingProperties
from .glue_target_processing_properties import GlueTargetProcessingProperties


class GlueUpdateIntegrationResourcePropertyRequest(BaseModel):
    ResourceArn: StrictStr
    SourceProcessingProperties: GlueSourceProcessingProperties | None = None
    TargetProcessingProperties: GlueTargetProcessingProperties | None = None
