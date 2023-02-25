from dataclasses import dataclass, field
from typing import Any, MutableMapping


@dataclass
class InstanceMap:
    _map: MutableMapping[Any, Any] = field(default_factory=dict)

    def chain(self) -> "InstanceMap":
        return InstanceMap({**self._map})

    def __contains__(self, target: Any) -> bool:
        return target in self._map

    def __getitem__(self, target: Any) -> Any:
        return self._map[target]

    def __setitem__(self, target: Any, value: Any) -> None:
        self._map[target] = value

    def __delitem__(self, target: Any) -> None:
        del self._map[target]

    def clear(self) -> None:
        self._map.clear()
