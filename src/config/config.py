from abc import abstractmethod
from typing import Any, Protocol

from src.models.config import HttpServer


class AbstractConfig(Protocol):
    @property
    @abstractmethod
    def http_server(self) -> HttpServer:
        raise NotImplementedError


class Config(AbstractConfig):
    def __init__(self, config_file: Any) -> None:
        self._config_file = config_file

    @property
    def http_server(self) -> HttpServer:
        return HttpServer(
            host=self._config_file["http_server"]["host"], port=self._config_file["http_server"]["port"]
        )
