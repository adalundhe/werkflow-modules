from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CopyFpgaImageRequest(BaseModel):
    SourceFpgaImageId: StrictStr
    SourceRegion: StrictStr
    DryRun: StrictBool | None = None
    Description: StrictStr | None = None
    Name: StrictStr | None = None
    ClientToken: StrictStr | None = None
