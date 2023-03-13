# Report
## Introduction
Nowadays the smart home devices play a fundamental role in everyday life, from the simple light that we can turn on with our smartphone to the home energy management (personal solar panel).
Since every of this device is connected to our network it is important to focus, not only on the speed of execution, but also on the privacy and the security features that the system should have.
Home Assistant was born with this goal. It is an open source software used for home automation of smart home devices with a focus on local control and privacy. 
On this software it is possible to use some integrations that define a specific device category of IoT devices in Home Assistant. There are many integrations provided by the community (since it is open source) but it is also possible to define some custom integrations.
There are different ways to use home assistant and in our case we use the Home Assistant Core based on devcontainer and Visual Studio Code.
Our goal is to develop three different integration on the Home Assistant platform:
### Listing
In this first integration we built an integration that had to print in the gateway console the list of all active integration.
First of all we need to build a button entity that can perform this operation.
### Emulated Light
In this second integration the goal was to emulate the manage of a light, not only with the turn on and the turn off, but the user must have the possibility to control the brightness of the light.
### Turn off all
In the last integration we need to develop a button on the dashboard of the Smart Home Gateway to turn off all the integrations that have the property on/off.


## Implementation
From the implementation point of view we develop three custom component:
- One Light
- Two Buttons

### Light
Since we didn't want only that the light just turn on and off, but we wanted only to control the brightness, in the initialization of the Light Entity we need to set the right flag that allow us to manage the brightness:
```
        self._attr_color_mode = ColorMode.BRIGHTNESS
        self._attr_supported_color_modes = [
            ColorMode.BRIGHTNESS,
            ColorMode.COLOR_TEMP,
            ColorMode.HS,
            ColorMode.WHITE,
        ]
```
Then we define the two different function:
- Turn on
- Turn off

In the "turn_on" function we change the state of the light, we put the brightness to a define value and then we check that the brightness of the light and the parameter of the brightness that came from the dashboard is the same. If it is not the same, this means that the user want to change the brightness of the light, so we update the value with the value setted by the user.

In the "turn_off" function we just put the state of the light to "False" and we set the brightness to "0".

### Button one
The first button was designed to list all the active integrations on Home Assistant.
We writed the press function (after the initialization) in which we print in the console gateway the list of integration.
This is done thanks to the "hass" object that permit us to access the data of the "Home Assistant Core" where we can see all the integrations.
Then we check that all the integrations are in the list of the components present inside Home Assistant.
```
        for domain in self.hass.data["integrations"]:
            integration = self.hass.data["integrations"][domain]
            if domain in self.hass.config.components:
                _LOGGER.info("%s\n", domain)
```

### Button two
In the second button we wanted to turn off all the integrations that have the on/off property.
But, first of all, we need to take the list of all the possible entities present inside Home Assistant and then we have to change the state of this entities thanks to the function "set"
```
        services = self.hass.states.entity_ids()
        for key in services:
            if self.hass.states.is_state(key, "on"):
                self.hass.states.set(key, "off")

                _LOGGER.info("%s\n", self.hass.states.get(key))
```

## Conclusion
This software it grants us full control, which is why it is very powerful since not all the software permit this. 
Also the possibility to have an higher level of privacy is a great point to focus on.
