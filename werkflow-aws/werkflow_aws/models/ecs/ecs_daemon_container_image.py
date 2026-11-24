from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDaemonContainerImage(BaseModel):
    containerName: StrictStr | None = None
    imageDigest: StrictStr | None = None
    image: StrictStr | None = None
