from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .work_spaces_image_source_identifier import WorkSpacesImageSourceIdentifier
from .work_spaces_tag import WorkSpacesTag


class WorkSpacesImportCustomWorkspaceImageRequest(BaseModel):
    ImageName: StrictStr
    ImageDescription: StrictStr
    ComputeType: Literal['BASE', 'GRAPHICS_G4DN', 'GRAPHICS_G6', 'GRAPHICS_G7']
    Protocol: Literal['PCOIP', 'DCV', 'BYOP']
    ImageSource: WorkSpacesImageSourceIdentifier
    InfrastructureConfigurationArn: StrictStr
    Platform: Literal['WINDOWS']
    OsVersion: Literal['Windows_10', 'Windows_11']
    Tags: list[WorkSpacesTag] | None = None
    ImageValidationMode: Literal['CUSTOMER_MANAGED', 'SERVICE_MANAGED'] | None = None
