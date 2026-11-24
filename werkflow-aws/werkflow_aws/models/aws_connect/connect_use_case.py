from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUseCase(BaseModel):
    UseCaseId: StrictStr | None = None
    UseCaseArn: StrictStr | None = None
    UseCaseType: StrictStr | None = None
