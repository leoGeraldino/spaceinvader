<h1>Welcome to the Space Invader game!</h1>

Are you ready for fun?<br>
So, before we continue, I need to explain some things to you...

<h2>How to play</h2>

After you download the repository, you must find a file called <b>spaceinvader.py</b>. You open and run it, so a new window called <i>Space Invader</i> will open.<br>
To control the spaceship, press the keys <kbd>A</kbd> and <kbd>D</kbd> on the keyboard, to move the ship to the left and to the right, respectivelly. <br> To shot against the aliens, you must press the keyboard space bar. <br>
If you want to change the controls, you must go to the lines 91 and 93, to change the direction buttons of the spaceship, by changing the event.key comparators, in the respective lines. If you want to change the shot button, you need to change the line 95, doing the same thing in the previous step<br>

For example, if you need to change all the controls for the spaceship, using left and right keys for the direction and up key for the shot, you must do something like the code below:
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
Note that if you do the changes above, you must change the event.key comparators in the line 104, to the respective keys you used before.<br>

Be carefully! When an alien comes to the same row that the spaceship be, you'll lost and it will be a game over. <br>

I hope you have fun!

<h2>Next development steps</h2>

I want to create levels for the game. I don't know exactly how it wil be, but I think in something like more aliens to shot, as the player scores. Maybe, I'll create a boss, when the player reach a certain score. Some obstacles like meteors or abandoned spaceships in the screen is the other resources that I want to improve in the game. Finally, I want to create a multiplayer mode, in which two players can play at the same time and screen.    
