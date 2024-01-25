from werkflow.modules.base import Module
from .services import (
    AWSCredentials,
    AWSCodeArtifact
)


class AWS(Module):

    def __init__(self) -> None:
        super().__init__()

        self.credentials = AWSCredentials()
        self.code_artifact = AWSCodeArtifact()

    async def close(self):
        await self.credentials.close()
        await self.code_artifact.close()

    def abort(self):
        self.credentials.abort()
        self.code_artifact.abort()

    

