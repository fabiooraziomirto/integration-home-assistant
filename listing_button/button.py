from __future__ import annotations
import logging

from homeassistant.core import HomeAssistant
from homeassistant.components.button import ButtonEntity
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType


DEFAULT_NAME = "Listing Button"


_LOGGER = logging.getLogger(__name__)


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    add_entities([ListingButton()])
    return True


class ListingButton(ButtonEntity):
    def __init__(self, name: str = DEFAULT_NAME) -> None:
        self._attr_name = name

    def press(self) -> None:
        integration = []

        for domain in self.hass.data["integrations"]:
            if domain in self.hass.config.components:
                integration.append(domain)

        integration.sort()

        _LOGGER.info("%s\n", integration)
