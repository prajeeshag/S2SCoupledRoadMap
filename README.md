# Development of the AP regional coupled model for S2S prediction

- [ ] Domain, Grid and Resolution
- [ ] Set up WRF and MITgcm in the new domain. Make standalone hindcasts and evaluate against the S2S models (Feb-March 2023)
- [ ] Setting up the coupled model and make test simulations (March-April 2023)
- [ ] Developing an end-to-end automated workflow using [CYLC](https://cylc.github.io) workflow engine (April-May 2023)
- [ ] Run hindcasts and evaluate against the standalone S2S models (June-August 2023)
- [ ] Optimize the coupled model for performance (September 2023)
- [ ] [Develop an automated evaluation framework] (October 2023)



## Domain, Grid and Resolution
The coupled model domain will be kept as similar as possible to the current standalone S2S model. The current S2S setup of WRF use  

![Current S2S domain]('assets/images/wps_dom_S2SWRF.png')