from __future__ import annotations

from typing import Any, Iterator, List, Optional, Tuple

from ..layers import (
    Add,
    Arg,
    Cmd,
    Copy,
    Entrypoint,
    Env,
    Expose,
    Healthcheck,
    Label,
    Maintainer,
    OnBuild,
    Run,
    Shell,
    Stage,
    StopSignal,
    User,
    Volume,
    Workdir,
)

LayerType = (
    Add
    | Arg
    | Cmd
    | Copy
    | Entrypoint
    | Env
    | Expose
    | Healthcheck
    | Label
    | Maintainer
    | OnBuild
    | Run
    | Shell
    | Stage
    | StopSignal
    | User
    | Volume
    | Workdir
)


class LayerQuery:

    def __init__(self, layers: List[LayerType]) -> None:
        self._layers = layers

    def __iter__(self) -> Iterator[LayerType]:
        for layer in self._layers:
            yield layer

    def get(
        self,
        attributes: Tuple[str, Any] | List[Tuple[str, Any]],
    ) -> LayerQuery:
        layers: List[LayerType] = []

        if not isinstance(attributes, list):
            attributes = [attributes]

        for layer in self._layers:
            layer_dict = layer.model_dump()

            for attribute, value in attributes:
                layer_attribute = layer_dict.get(attribute)

                if isinstance(layer_attribute, list) and value in layer_attribute:
                    layers.append(layer)
                elif isinstance(layer_attribute, dict) and (
                    value in layer_attribute or value in list(layer_attribute.values())
                ):
                    layers.append(layer)
                elif layer_attribute == value:
                    layers.append(layer)

        return LayerQuery(layers)

    def results(self) -> List[LayerType]:
        return self._layers

    def one(self) -> Optional[LayerType]:
        if len(self._layers) > 0:
            return self._layers.pop()
        return None
