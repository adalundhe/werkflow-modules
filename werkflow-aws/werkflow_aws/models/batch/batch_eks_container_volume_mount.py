from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BatchEksContainerVolumeMount(BaseModel):
    name: StrictStr | None = None
    mountPath: StrictStr | None = None
    subPath: StrictStr | None = None
    readOnly: StrictBool | None = None
