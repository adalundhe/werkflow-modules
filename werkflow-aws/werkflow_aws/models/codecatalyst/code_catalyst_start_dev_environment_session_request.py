from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_catalyst_dev_environment_session_configuration import CodeCatalystDevEnvironmentSessionConfiguration


class CodeCatalystStartDevEnvironmentSessionRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr
    id: StrictStr
    sessionConfiguration: CodeCatalystDevEnvironmentSessionConfiguration
