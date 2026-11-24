from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_delete_volume_ontap_response import FSxDeleteVolumeOntapResponse


class FSxDeleteVolumeResponse(BaseModel):
    VolumeId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    OntapResponse: FSxDeleteVolumeOntapResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
