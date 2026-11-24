from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchPackageConfiguration(BaseModel):
    LicenseRequirement: StrictStr | None = None
    LicenseFilepath: StrictStr | None = None
    ConfigurationRequirement: StrictStr | None = None
    RequiresRestartForConfigurationUpdate: StrictBool | None = None
