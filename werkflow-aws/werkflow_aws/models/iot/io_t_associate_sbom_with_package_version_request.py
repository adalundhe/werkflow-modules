from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_sbom import IoTSbom


class IoTAssociateSbomWithPackageVersionRequest(BaseModel):
    packageName: StrictStr
    versionName: StrictStr
    sbom: IoTSbom
    clientToken: StrictStr | None = None
