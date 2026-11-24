from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_package_version_artifact import IoTPackageVersionArtifact


class IoTCreatePackageVersionRequest(BaseModel):
    packageName: StrictStr
    versionName: StrictStr
    description: StrictStr | None = None
    attributes: dict[StrictStr, StrictStr] | None = None
    artifact: IoTPackageVersionArtifact | None = None
    recipe: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    clientToken: StrictStr | None = None
