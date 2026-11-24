from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .app_runner_authentication_configuration import AppRunnerAuthenticationConfiguration
from .app_runner_code_repository import AppRunnerCodeRepository
from .app_runner_image_repository import AppRunnerImageRepository


class AppRunnerSourceConfiguration(BaseModel):
    CodeRepository: AppRunnerCodeRepository | None = None
    ImageRepository: AppRunnerImageRepository | None = None
    AutoDeploymentsEnabled: StrictBool | None = None
    AuthenticationConfiguration: AppRunnerAuthenticationConfiguration | None = None
