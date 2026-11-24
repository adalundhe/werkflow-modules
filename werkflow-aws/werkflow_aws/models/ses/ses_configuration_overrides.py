from __future__ import annotations
from pydantic import BaseModel
from .ses_tracking_configuration_overrides import SESTrackingConfigurationOverrides


class SESConfigurationOverrides(BaseModel):
    Tracking: SESTrackingConfigurationOverrides | None = None
