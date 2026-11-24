from __future__ import annotations
from pydantic import BaseModel
from .athena_result_reuse_by_age_configuration_model import AthenaResultReuseByAgeConfigurationModel


class AthenaResultReuseConfigurationModel(BaseModel):
    ResultReuseByAgeConfiguration: AthenaResultReuseByAgeConfigurationModel | None = None
