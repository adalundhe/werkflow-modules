from werkflow.modules.base import Module
from .services import (
    AWSCredentials,
    AWSCodeArtifact,
    AWSCostExplorer,
    AWSElastiCache,
)


class AWS(Module):

    def __init__(self) -> None:
        super().__init__()

        self.credentials = AWSCredentials()
        self.code_artifact = AWSCodeArtifact()
        self.cost_explorer = AWSCostExplorer()
        self.elasticache = AWSElastiCache()

    async def close(self):
        await self.credentials.close()
        await self.code_artifact.close()
        await self.cost_explorer.close()
        await self.elasticache.close()

    def abort(self):
        self.credentials.abort()
        self.code_artifact.abort()
        self.cost_explorer.abort()
        self.elasticache.abort()

    

