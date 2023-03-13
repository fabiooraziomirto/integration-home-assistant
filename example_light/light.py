from __future__ import annotations
import logging

from homeassistant.core import HomeAssistant
from homeassistant.components.light import LightEntity
from homeassistant.components.light import (
    ATTR_BRIGHTNESS_PCT,
    ColorMode,
    SUPPORT_BRIGHTNESS,
)
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

DEFAULT_NAME = "Example Light"


_LOGGER = logging.getLogger(__name__)


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    name = DEFAULT_NAME

    add_entities([ExampleLight(name)])
    return True


class ExampleLight(LightEntity):
    def __init__(self, name: str = DEFAULT_NAME) -> None:
        self._name = name
        self._state = False
        self._brightness = None
        self._attr_color_mode = ColorMode.BRIGHTNESS
        self._attr_supported_color_modes = [
            ColorMode.BRIGHTNESS,
            ColorMode.COLOR_TEMP,
            ColorMode.HS,
            ColorMode.WHITE,
        ]

    @property
    def name(self) -> str:
        return self._name

    @property
    def brightness(self):
        return self._brightness

    @property
    def is_on(self) -> bool | None:
        return self._state

    @property
    def supported_features(self) -> int:
        return SUPPORT_BRIGHTNESS

    def turn_on(self, **kwargs):
        brightness = kwargs.get(ATTR_BRIGHTNESS_PCT, 255)
        self._brightness = brightness
        self._state = True
        _LOGGER.info("Light on %s %s\n", self._brightness, kwargs.get("brightness"))

        if (
            self._brightness != kwargs.get("brightness")
            and kwargs.get("brightness") is not None
        ):
            self._brightness = kwargs.get("brightness")
            _LOGGER.info(
                "Update brightness %s %s\n", self._brightness, kwargs.get("brightness")
            )

    def turn_off(self, **kwargs):
        if self.is_on is True:
            self._state = False
            self._brightness = 0
            self.hass.states.set("light.example_light", "off")
            _LOGGER.info("%s\n", self.hass.states.get("light.example_light"))
            _LOGGER.info("Light off %s\n", self._state)
