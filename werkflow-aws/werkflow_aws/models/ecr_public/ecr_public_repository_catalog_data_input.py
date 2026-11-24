from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class ECRPublicRepositoryCatalogDataInput(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    description: StrictStr | None = None
    architectures: list[StrictStr] | None = None
    operatingSystems: list[StrictStr] | None = None
    logoImageBlob: StrictBytes | BinaryIO | StrictStr | None = None
    aboutText: StrictStr | None = None
    usageText: StrictStr | None = None
