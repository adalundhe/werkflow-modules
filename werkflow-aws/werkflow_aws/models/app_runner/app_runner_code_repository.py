from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_runner_code_configuration import AppRunnerCodeConfiguration
from .app_runner_source_code_version import AppRunnerSourceCodeVersion


class AppRunnerCodeRepository(BaseModel):
    RepositoryUrl: StrictStr | None = None
    SourceCodeVersion: AppRunnerSourceCodeVersion | None = None
    CodeConfiguration: AppRunnerCodeConfiguration | None = None
    SourceDirectory: StrictStr | None = None
