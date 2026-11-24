from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .work_spaces_tag import WorkSpacesTag


class WorkSpacesImportWorkspaceImageRequest(BaseModel):
    Ec2ImageId: StrictStr
    IngestionProcess: Literal['BYOL_REGULAR', 'BYOL_GRAPHICS', 'BYOL_GRAPHICSPRO', 'BYOL_GRAPHICS_G4DN', 'BYOL_REGULAR_WSP', 'BYOL_GRAPHICS_G4DN_WSP', 'BYOL_REGULAR_BYOP', 'BYOL_GRAPHICS_G4DN_BYOP']
    ImageName: StrictStr
    ImageDescription: StrictStr
    Tags: list[WorkSpacesTag] | None = None
    Applications: list[Literal['Microsoft_Office_2016', 'Microsoft_Office_2019']] | None = None
