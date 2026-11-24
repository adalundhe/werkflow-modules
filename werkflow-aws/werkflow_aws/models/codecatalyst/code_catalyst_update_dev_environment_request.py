from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .code_catalyst_ide_configuration import CodeCatalystIdeConfiguration


class CodeCatalystUpdateDevEnvironmentRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr
    id: StrictStr
    alias: StrictStr | None = None
    ides: list[CodeCatalystIdeConfiguration] | None = None
    instanceType: Literal['dev.standard1.small', 'dev.standard1.medium', 'dev.standard1.large', 'dev.standard1.xlarge'] | None = None
    inactivityTimeoutMinutes: StrictInt | None = None
    clientToken: StrictStr | None = None
