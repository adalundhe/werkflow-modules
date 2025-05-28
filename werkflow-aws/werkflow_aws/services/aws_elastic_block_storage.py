import asyncio
from concurrent.futures import ThreadPoolExecutor
from werkflow_aws.models import AWSRegionMap
from werkflow_system import System


class AWSElasticBlockStorage:
    
    def __init__(self) -> None:
        
        self._system = System()

        self._loop: asyncio.AbstractEventLoop | None = None
        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

        self._client = None

        self.service_name = 'ElasticBlockStorage'
        self._regions = AWSRegionMap()