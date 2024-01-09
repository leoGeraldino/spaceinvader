<h1>Welcome to the Space Invader game!</h1>

Are you ready for fun?<br>
So, before we continue, I need to explain some things to you...

<h2>How to play</h2>

After you download the repository, you must find a file called <b>spaceinvader.py</b>. Open and run it, and a new window called <i>Space Invader</i> will open.<br>
To control the spaceship, press the keys <kbd>A</kbd> and <kbd>D</kbd> on the keyboard, to move the ship to the left and right, respectively. <br> 
To shoot against the aliens, press the space bar on the keyboard. <br>
If you want to change the controls, you must go to lines 91 and 93, to change the direction buttons of the spaceship by modifying the event.key comparators, in the respective lines. If you want to change the shot button, modify line 95, following the same steps as in the the previous instruction.<br>

For example, if you need to change all the controls for the spaceship, using the left and right keys for direction and up key for the shot, you must do something like the code below:
```
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: 
                playerX_change = -5
            if event.key == pygame.K_RIGHT: 
                playerX_change = 5
            if event.key == pygame.K_UP: 
                if bullet_state == "pronto":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX 
                    bullet_state = "fogo"
                    fire_bullet(bulletX, bulletY)
```
Note that if you make the changes above, you must modify the event.key comparators in line 104, to the respective keys you used before.<br>

Be carefully! When an alien comes to the same row as the spaceship, you will lose and it will be a game over. <br>

I hope you have fun!

<h2>Next development steps</h2>

I want to create levels for the game. I don't know exactly how it will be, but I'm thinking of something like more aliens to shoot as the player scores. Maybe I'll create a boss when the player reach a certain score. Some obstacles like meteors or abandoned spaceships on the screen are the other resources that I want to improve in the game. Finally, I want to create a multiplayer mode in which two players can play at the same time on the screen.    
