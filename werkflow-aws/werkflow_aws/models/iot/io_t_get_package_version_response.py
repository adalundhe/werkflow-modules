from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_package_version_artifact import IoTPackageVersionArtifact
from .io_t_sbom import IoTSbom


class IoTGetPackageVersionResponse(BaseModel):
    packageVersionArn: StrictStr | None = None
    packageName: StrictStr | None = None
    versionName: StrictStr | None = None
    description: StrictStr | None = None
    attributes: dict[StrictStr, StrictStr] | None = None
    artifact: IoTPackageVersionArtifact | None = None
    status: StrictStr | None = None
    errorReason: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    sbom: IoTSbom | None = None
    sbomValidationStatus: StrictStr | None = None
    recipe: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
