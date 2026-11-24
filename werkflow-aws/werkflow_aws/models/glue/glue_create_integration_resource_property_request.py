from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_source_processing_properties import GlueSourceProcessingProperties
from .glue_tag import GlueTag
from .glue_target_processing_properties import GlueTargetProcessingProperties


class GlueCreateIntegrationResourcePropertyRequest(BaseModel):
    ResourceArn: StrictStr
    SourceProcessingProperties: GlueSourceProcessingProperties | None = None
    TargetProcessingProperties: GlueTargetProcessingProperties | None = None
    Tags: list[GlueTag] | None = None
