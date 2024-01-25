from abc import ABC, abstractmethod
from typing import Dict


class CodeArtifactClient(ABC):

    @abstractmethod
    def get_authorization_token(
        self,
        domain: str=None,
        domainOwner: str=None,
        durationSeconds: int=None
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def get_repository_endpoint(
        self,
        domain: str=None,
        domainOwner: str=None,
        repository: str=None,
        format: str=None
    ) -> Dict[str, str]:
        pass

    @abstractmethod
    def close(self):
        pass