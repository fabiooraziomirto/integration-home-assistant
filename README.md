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
