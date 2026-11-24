from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .io_t_package_version_artifact import IoTPackageVersionArtifact


class IoTUpdatePackageVersionRequest(BaseModel):
    packageName: StrictStr
    versionName: StrictStr
    description: StrictStr | None = None
    attributes: dict[StrictStr, StrictStr] | None = None
    artifact: IoTPackageVersionArtifact | None = None
    action: Literal['PUBLISH', 'DEPRECATE'] | None = None
    recipe: StrictStr | None = None
    clientToken: StrictStr | None = None
