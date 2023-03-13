from __future__ import annotations
import logging

from homeassistant.core import HomeAssistant
from homeassistant.components.button import ButtonEntity
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

DEFAULT_NAME = "Example Button"


_LOGGER = logging.getLogger(__name__)


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    add_entities([ExampleButton()])
    return True


class ExampleButton(ButtonEntity):
    def __init__(self, name: str = DEFAULT_NAME) -> None:
        self._attr_name = name
        _LOGGER.debug("Button 1 initialized\n")

    def press(self) -> None:
        """Handle the button press."""
        _LOGGER.info("Button 1 pressed\n")

        for domain in self.hass.data["integrations"]:
            integration = self.hass.data["integrations"][domain]
            if domain in self.hass.config.components:
                _LOGGER.info("%s\n", domain)
