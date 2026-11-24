from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_event_metadata import SageMakerEventMetadata


class SageMakerEventDetails(BaseModel):
    EventMetadata: SageMakerEventMetadata | None = None
