from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_runner_image_configuration import AppRunnerImageConfiguration


class AppRunnerImageRepository(BaseModel):
    ImageIdentifier: StrictStr | None = None
    ImageConfiguration: AppRunnerImageConfiguration | None = None
    ImageRepositoryType: StrictStr | None = None
