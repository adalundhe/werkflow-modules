from __future__ import annotations
from abc import ABC, abstractmethod
from typing import (
    Any
)


class SecretsManagerClient(ABC):

    @abstractmethod
    def get_secret_value(
        self,
        SecretId: str = None,
        VersionId: str | None = None,
        VersionStage: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def close(self):
        pass