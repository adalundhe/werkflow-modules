from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_recording_group import ConfigServiceRecordingGroup
from .config_service_recording_mode import ConfigServiceRecordingMode
from .config_service_scope_configuration import ConfigServiceScopeConfiguration


class ConfigServiceConfigurationRecorder(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    roleARN: StrictStr | None = None
    recordingGroup: ConfigServiceRecordingGroup | None = None
    recordingMode: ConfigServiceRecordingMode | None = None
    recordingScope: StrictStr | None = None
    servicePrincipal: StrictStr | None = None
    connectorArn: StrictStr | None = None
    scopeConfiguration: ConfigServiceScopeConfiguration | None = None
