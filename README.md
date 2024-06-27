# IcosaHarengon

My personal web app for running D&D 5e games with the help of a VTT!

## About

This project is intended to be a solution for virtualization of TTRPG play, including online play, and is intended to be used in conjunction with [Planar Ally](https://www.planarally.io/) or a similar virtual tabletop.

IcosaHarengon provides functionality for recording game data, including character sheets, monster stat blocks, compendiums, and customizable notes, integrated with a templatable dice-rolling engine. Groups can utilize this tool by connecting to the application's web interface. 

## Development Notes

### Application Structure Outline

#### Core Components

- Abstract templated objects
    - Pre-defined templates
    - Custom templating option
- Abstract game object
- Command/chat log
    - Interaction API
    - History record
- UI
- Database
    - User database
    - Game database
        - Templated object database
        - History record database
        - (User database links)