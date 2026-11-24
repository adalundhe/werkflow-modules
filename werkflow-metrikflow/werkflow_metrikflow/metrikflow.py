import datetime
import json
from typing import Any, Dict, List, Literal, Optional, Union

from werkflow_core import Module
from werkflow_core.exceptions.missing_module_error import MissingModuleError
from werkflow_shell import Shell

try:
    from metrikflow.connectors import AsyncConnector
    from metrikflow.connectors.connector import ConnectorTypes
    from metrikflow.dashboards import Dashboard
    from metrikflow.metrics import MetricStore
    from metrikflow.metrics.types import Event, Interval, Rate

    module_enabled = True
except ImportError:
    module_enabled = False
    AsyncConnector = None  # type: ignore[assignment,misc]
    ConnectorTypes = None  # type: ignore[assignment,misc]
    Dashboard = None  # type: ignore[assignment,misc]
    MetricStore = None  # type: ignore[assignment,misc]
    Event = None  # type: ignore[assignment,misc]
    Interval = None  # type: ignore[assignment,misc]
    Rate = None  # type: ignore[assignment,misc]


MetricKind = Literal['event', 'interval', 'rate']
MetricUnit = Literal[
    'nanoseconds',
    'microseconds',
    'milliseconds',
    'seconds',
    'minutes',
    'hours',
    'days',
    'weeks',
]


class Metrik(Module):
    module_enabled = module_enabled
    dependencies = [
        'datadog-api-client',
        'metrikflow',
        'werkflow-shell',
    ]

    def __init__(self) -> None:
        super().__init__()
        self._store: Any = MetricStore() if MetricStore is not None else None
        self._loader: Any = AsyncConnector() if AsyncConnector is not None else None
        self._sender: Any = AsyncConnector() if AsyncConnector is not None else None
        self.dashboards: Any = Dashboard() if Dashboard is not None else None

        self.sender_config: Dict[str, Any] = {}
        self.loader_config: Dict[str, Any] = {}
        self._loader_connected: bool = False
        self._sender_connected: bool = False
        self._closed: bool = False

        self.load_uri: Optional[str] = None
        self.send_uri: Optional[str] = None
        self.loader_type: Optional[str] = None
        self.sender_type: Optional[str] = None

        self._shell = Shell()

    def _ensure_enabled(self) -> None:
        if not self.module_enabled:
            raise MissingModuleError(self)

    async def connect_loader(
        self,
        connector_type: str,
        uri: str,
        config_path: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        self._ensure_enabled()
        self.loader_type = connector_type
        self.load_uri = uri

        if config_path:
            resolved_path = await self._shell.to_absolute_path(config_path)
            loader_config = await self._shell.read_file(
                resolved_path,
                silent=True,
            )
            self.loader_config.update(json.loads(loader_config))

        self.loader_config.update(kwargs)

        await self._loader.connect(
            self.loader_type,
            **self.loader_config,
        )
        self._loader_connected = True
        self._closed = False

    async def connect_sender(
        self,
        connector_type: str,
        uri: str,
        config_path: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        self._ensure_enabled()
        self.sender_type = connector_type
        self.send_uri = uri

        if config_path:
            resolved_path = await self._shell.to_absolute_path(config_path)
            sender_config = await self._shell.read_file(
                resolved_path,
                silent=True,
            )
            self.sender_config.update(json.loads(sender_config))

        self.sender_config.update(kwargs)

        await self._sender.connect(
            self.sender_type,
            **self.sender_config,
        )
        self._sender_connected = True
        self._closed = False

    async def record_metric(
        self,
        name: str,
        kind: MetricKind,
        timestamp: Optional[datetime.datetime] = None,
        value: Union[int, float, None] = None,
        group: str = 'default',
        tags: Optional[List[Dict[str, str]]] = None,
        unit: Optional[MetricUnit] = None,
    ) -> Any:
        self._ensure_enabled()
        if timestamp is None:
            timestamp = datetime.datetime.now(datetime.timezone.utc)

        record_kwargs: Dict[str, Any] = {
            'name': name,
            'kind': kind,
            'group': group,
            'timestamp': timestamp,
            'value': value,
            'tags': tags,
        }
        if unit is not None:
            record_kwargs['unit'] = unit

        return self._store.record(**record_kwargs)

    async def load_metric(
        self,
        name: str,
        kind: MetricKind,
        value: Union[int, float, None] = None,
        group: str = 'default',
        timeout: Union[int, float] = 60,
    ) -> Any:
        self._ensure_enabled()
        if not self._loader_connected or self.load_uri is None:
            raise RuntimeError('Loader is not connected. Call connect_loader() first.')

        load_query = self._store.create_load_query(
            name=name,
            kind=kind,
            group=group,
            timestamp=datetime.datetime.now(datetime.timezone.utc),
            value=value,
        )

        return await self._loader.load(
            self.load_uri,
            load_query,
            timeout=timeout,
        )

    async def send_metric(
        self,
        metric: List[Any],
        timeout: Union[int, float] = 60,
    ) -> None:
        self._ensure_enabled()
        if (
            not self._sender_connected
            or self.send_uri is None
            or self.sender_type is None
        ):
            raise RuntimeError('Sender is not connected. Call connect_sender() first.')

        file_connector_types = (
            (ConnectorTypes.CSV, ConnectorTypes.JSON, ConnectorTypes.XML)
            if ConnectorTypes is not None
            else ()
        )

        if self._sender.selected_connector_type in file_connector_types:
            await self.connect_sender(
                self.sender_type,
                self.send_uri,
            )

            await self._sender.send(
                self.send_uri,
                metric,
                timeout=timeout,
            )

            await self._sender.close()
        else:
            await self._sender.send(
                self.send_uri,
                metric,
                timeout=timeout,
            )

    async def close(self) -> None:
        if self._loader is not None:
            try:
                await self._loader.close()
            except Exception:
                pass

        if self._sender is not None:
            try:
                await self._sender.close()
            except Exception:
                pass

        await self._shell.close()
        self._loader_connected = False
        self._sender_connected = False
        self._closed = True

    def abort(self) -> None:
        self._shell.abort()
        self._loader_connected = False
        self._sender_connected = False
        self._closed = True
