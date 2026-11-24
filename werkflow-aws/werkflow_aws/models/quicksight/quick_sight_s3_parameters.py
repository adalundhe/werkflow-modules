from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_manifest_file_location import QuickSightManifestFileLocation


class QuickSightS3Parameters(BaseModel):
    ManifestFileLocation: QuickSightManifestFileLocation | None = None
    RoleArn: StrictStr | None = None
