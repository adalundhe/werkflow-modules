from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_stream_error_details import AppStreamErrorDetails


class AppStreamSoftwareAssociations(BaseModel):
    SoftwareName: StrictStr | None = None
    Status: StrictStr | None = None
    DeploymentError: list[AppStreamErrorDetails] | None = None
