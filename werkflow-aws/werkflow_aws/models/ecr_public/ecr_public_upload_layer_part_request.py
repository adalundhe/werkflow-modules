from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictInt, StrictStr


class ECRPublicUploadLayerPartRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    repositoryName: StrictStr
    uploadId: StrictStr
    partFirstByte: StrictInt
    partLastByte: StrictInt
    layerPartBlob: StrictBytes | BinaryIO | StrictStr
    registryId: StrictStr | None = None
