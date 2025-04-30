import datetime
import json
from typing import Any, Dict, List, Literal, Optional, Union

from metrikflow.connectors import AsyncConnector
from metrikflow.connectors.connector import ConnectorTypes
from metrikflow.dashboards import Dashboard
from metrikflow.metrics import MetricStore
from metrikflow.metrics.types import Event, Interval, Rate
from werkflow_core import Module
from werkflow_shell import Shell


class Metrik(Module):

    def __init__(self) -> None:
        super().__init__()
        self._store = MetricStore()
        self._loader = AsyncConnector()
        self._sender = AsyncConnector()
        
        self.dashboards = Dashboard()

        self.sender_config: Dict[str, Any] = {}
        self.loader_config: Dict[str, Any] = {}
        self._sender_connected: bool =False
        self._closed: bool = False

        self.load_uri: Union[
            str,
            None
        ] = None

        self.send_uri: Union[
            str,
            None
        ] = None

        self.loader_type: Union[
            str,
            None
        ] = None

        self.sender_type: Union[
            str,
            None
        ] = None

        self._shell = Shell()

    async def connect_loader(
        self,
        connector_type: str,
        uri: str,
        config_path: Optional[str]=None,
        **kwargs
    ):
        
        self.loader_type = connector_type
        self.load_uri = uri
        
        if config_path:

            config_path = await self._shell.to_absolute_path(config_path)

            loader_config = await self._shell.read_file(
                config_path,
                silent=True
            )
        
            self.loader_config.update(
                json.loads(loader_config)
            )

        self.loader_config.update(kwargs)

        await self._loader.connect(
            self.loader_type,
            **self.loader_config
        )

    async def connect_sender(
        self,
        connector_type: str,
        uri: str,
        config_path: Optional[str]=None,
        **kwargs
    ):
        self.sender_type = connector_type
        self.send_uri = uri
        
        if config_path:

            config_path = await self._shell.to_absolute_path(config_path)

            sender_config = await self._shell.read_file(
                config_path,
                silent=True
            )
        
            self.loader_config.update(
                json.loads(sender_config)
            )

        self.sender_config.update(kwargs)

        await self._sender.connect(
            self.sender_type,
            **self.sender_config
        )

    async def record_metric(
        self,
        name: str,
        kind: Union[
            Literal['event'],
            Literal['interval'],
            Literal['rate']
        ],
        timestamp: Optional[
            datetime.datetime
        ] = None,
        value: Union[
            int,
            float
        ]=None,
        group: str='default',
        tags: Optional[
            List[Dict[str, str]]
        ]=None,
        unit: Literal[
            'nanoseconds',
            'microseconds',
            'milliseconds',
            'seconds',
            'minutes',
            'hours',
            'days',
            'weeks'
        ]=None
    ):
        
        if timestamp is None:
            timestamp = datetime.datetime.now(datetime.timezone.utc)

        return self._store.record(
            name=name,
            kind=kind,
            group=group,
            timestamp=timestamp,
            value=value,
            tags=tags
        )

    async def load_metric(
        self,
        name: str,
        kind: Union[
            Literal['event'],
            Literal['interval'],
            Literal['rate']
        ],
        value: Union[
            int,
            float
        ]=None,
        group: str='default',
        timeout: Union[
            int,
            float
        ]=60
    ):
        
        load_query = self._store.create_load_query(
            name=name,
            kind=kind,
            group=group,
            timestamp=datetime.datetime.now(
                datetime.timezone.utc
            ),
            value=value
        )

        return await self._loader.load(
            self.load_uri,
            load_query,
            timeout=timeout
        )

    async def send_metric(
        self,
        metric: List[
            Union[
                Event,
                Interval,
                Rate
            ]
        ],
        timeout: Union[
            int,
            float
        ]=60
    ):
        
        if self._sender.selected_connector_type in [
            ConnectorTypes.CSV,
            ConnectorTypes.JSON,
            ConnectorTypes.XML
        ]:
            
            await self.connect_sender(
                self.sender_type,
                self.send_uri
            )

            await self._sender.send(
                self.send_uri,
                metric,
                timeout=timeout
            )

            await self._sender.close()
        
        else:

            await self._sender.send(
                self.send_uri,
                metric,
                timeout=timeout
            )

    async def close(self):
        await self._loader.close()
        await self._sender.close()