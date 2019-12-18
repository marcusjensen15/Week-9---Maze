Maze
Create a Sinatra application with CRUD functionality where users can traverse a maze. Each "room" of the maze should have a description and one or more ways to move to another room. For instance, if the room is a dead end, then a user should be able to return to the previous room. There could be a winning condition if the user successfully traverses the maze.

Start by building a maze with a few hard-coded rooms. Use a whiteboard to visualize your maze before building it. Then add CRUD functionality so users can add more rooms to the maze.
Add objects with their own descriptions to the rooms. This will involve nested routing - for instance, an object belongs to a room. For a user to look at it, they might have to navigate to /rooms/7/objects/3.
Add an additional layer of complexity to your application. Allow a user to pick up items from various rooms of the maze. Some of these items (such as a key or a flashlight) might be necessary to successfully escape.
Add levers to some of the rooms. A user will only be able to pass through the door to the exit if the levers are in a certain position.
Continue to build out your maze in any way you like!
