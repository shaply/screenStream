# screenStream

## Description
Personal project where I create a streaming website/service

### 1. First attempt: Branch "Continuos-jpeg-transmissions-with-flask"
I tried to accomplish this task with flask and continuous screenshots. I created a class that continuously takes screenshots, saves them as jpegs, and then sends the images to the website. The class, screen, calls method capture as a thread, that way it can be run with the flask website code. 
The problem with this code is that since it uses jpeg transmissions, the speed of the streaming is very slow, and the client needs to continuously request for new images to recieve them. 
