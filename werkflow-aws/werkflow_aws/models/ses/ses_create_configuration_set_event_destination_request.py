from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_event_destination_definition import SESEventDestinationDefinition


class SESCreateConfigurationSetEventDestinationRequest(BaseModel):
    ConfigurationSetName: StrictStr
    EventDestinationName: StrictStr
    EventDestination: SESEventDestinationDefinition
