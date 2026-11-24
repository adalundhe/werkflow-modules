from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .code_catalyst_ide_configuration import CodeCatalystIdeConfiguration
from .code_catalyst_persistent_storage_configuration import CodeCatalystPersistentStorageConfiguration
from .code_catalyst_repository_input import CodeCatalystRepositoryInput


class CodeCatalystCreateDevEnvironmentRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr
    instanceType: Literal['dev.standard1.small', 'dev.standard1.medium', 'dev.standard1.large', 'dev.standard1.xlarge']
    persistentStorage: CodeCatalystPersistentStorageConfiguration
    repositories: list[CodeCatalystRepositoryInput] | None = None
    clientToken: StrictStr | None = None
    alias: StrictStr | None = None
    ides: list[CodeCatalystIdeConfiguration] | None = None
    inactivityTimeoutMinutes: StrictInt | None = None
    vpcConnectionName: StrictStr | None = None
