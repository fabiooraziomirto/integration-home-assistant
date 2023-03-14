from __future__ import annotations
import logging

from homeassistant.core import HomeAssistant
from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

DEFAULT_NAME = "Example Switch"


_LOGGER = logging.getLogger(__name__)


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    name = DEFAULT_NAME

    add_entities([ExampleSwitch(name)])
    return True


class ExampleSwitch(SwitchEntity):
    def __init__(self, name: str = DEFAULT_NAME) -> None:
        self._name = name
        self._state = False

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_on(self) -> bool | None:
        return self._state

    def turn_on(self, **kwargs):
        self._state = True

    def turn_off(self, **kwargs):
        if self.is_on is True:
            self._state = False
