from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EC2DiskImageDetail(BaseModel):
    Format: Literal['VMDK', 'RAW', 'VHD']
    Bytes: StrictInt
    ImportManifestUrl: StrictStr
