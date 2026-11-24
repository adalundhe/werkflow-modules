from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_destination import IoTDestination
from .io_t_signing_profile_parameter import IoTSigningProfileParameter


class IoTStartSigningJobParameter(BaseModel):
    signingProfileParameter: IoTSigningProfileParameter | None = None
    signingProfileName: StrictStr | None = None
    destination: IoTDestination | None = None
