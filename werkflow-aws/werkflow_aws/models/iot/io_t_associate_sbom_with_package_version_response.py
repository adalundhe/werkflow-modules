from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_sbom import IoTSbom


class IoTAssociateSbomWithPackageVersionResponse(BaseModel):
    packageName: StrictStr | None = None
    versionName: StrictStr | None = None
    sbom: IoTSbom | None = None
    sbomValidationStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
