# Report
## Introduction
Nowadays smart home devices play a fundamental role in everyday life, from the simple light that we can turn on with our smartphone to home energy management (personal solar panel). Since every one of these devices is connected to our network it is important to focus, not only on the speed of the execution but also on the privacy and the security features that the system should have. Home Assistant was born with this goal. It is an open-source software used for home automation of smart home devices with a focus on local control and privacy. On this software, it is possible to use some integrations that define a specific device category of IoT devices in Home Assistant. There are many integrations provided by the community (since it is open source) but it is also possible to define some custom integrations. There are different ways to use a home assistant and in our case, we use the Home Assistant Core based on dev-container and Visual Studio Code. Our goal is to develop three different integration on the Home Assistant platform:
### Listing
In this first integration, we built an integration that had to print in the gateway console the list of all active integration. First of all, we need to build a button entity that can perform this operation.
### Emulated Light
In this second integration, the goal was to emulate the management of light, not only with the turn-on and the turn-off, but the user must have the possibility to control the brightness of the light.
### Turn off all
In the last integration, we need to develop a button on the dashboard of the Smart Home Gateway to turn off all the integrations that have the property on/off.


## Implementation
From the implementation point of view, we develop three custom components:
- One Light
- Two Buttons

### Light
Since we didn't want only the light just turns on and off, but we wanted only to control the brightness, in the initialization of the Light Entity we need to set the right flag that allows us to manage the brightness:
```
        self._attr_color_mode = ColorMode.BRIGHTNESS
        self._attr_supported_color_modes = [
            ColorMode.BRIGHTNESS,
            ColorMode.COLOR_TEMP,
            ColorMode.HS,
            ColorMode.WHITE,
        ]
```
Then we define the two different functions:
- Turn on
- Turn off

In the "turn_on" function we change the state of the light, we put the brightness to a defined value and then we check that the brightness of the light and the parameter of the brightness that came from the dashboard is the same. If it is not the same, this means that the user wants to change the brightness of the light, so we update the value with the value set by the user.

In the "turn_off" function we just put the state of the light to "False" and set the brightness to "0".

### Button one
The first button was designed to list all the active integrations on Home Assistant. We wrote the press function (after the initialization) in which we print in the console gateway the list of integration. This is done thanks to the "hass" object that permits us to access the data of the "Home Assistant Core" where we can see all the integrations. 
Then we check that all the integrations are in the list of the components present inside Home Assistant, in this way we can delete all the components that are not integrations.
```
        for domain in self.hass.data["integrations"]:
            if domain in self.hass.config.components:
                integration.append(domain)
```

### Button two
In the second button, we wanted to turn off all the integrations that have the on/off property. 
But, first of all, we need to take the list of all the possible entities that have a service called "turn_off" present inside Home Assistant and then we have to call this service to turn_off all this entities.
Since we need both the domain of the entities and the entity_id, we used the function "split_entity_id" that split the entity_id in two part: domain and object ID.
```
        entities = self.hass.states.entity_ids()
        for key in entities:
            domain = split_entity_id(key)
            if self.hass.services.has_service(domain=domain[0], service="turn_off"):
                self.hass.services.call(
                    domain=domain[0],
                    service="turn_off",
                    target={"entity_id": key},
                )

```

## Conclusion
This software grants us full control, which is why it is very powerful since not all the software permits this. Also, the possibility to have a higher level of privacy is a great point to focus on. In our case, we build only a few components, but Home Assistant gives us more features (automation, scripting, and also the management of secrets).
