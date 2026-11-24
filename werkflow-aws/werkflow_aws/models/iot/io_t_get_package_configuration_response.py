from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_version_update_by_jobs_config import IoTVersionUpdateByJobsConfig


class IoTGetPackageConfigurationResponse(BaseModel):
    versionUpdateByJobsConfig: IoTVersionUpdateByJobsConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
