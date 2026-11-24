from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_version_update_by_jobs_config import IoTVersionUpdateByJobsConfig


class IoTUpdatePackageConfigurationRequest(BaseModel):
    versionUpdateByJobsConfig: IoTVersionUpdateByJobsConfig | None = None
    clientToken: StrictStr | None = None
