from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_event_source_mapping_configuration import LambdaEventSourceMappingConfiguration


class LambdaListEventSourceMappingsResponse(BaseModel):
    NextMarker: StrictStr | None = None
    EventSourceMappings: list[LambdaEventSourceMappingConfiguration] | None = None
