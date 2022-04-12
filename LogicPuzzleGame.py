import pygame, sys
from buttonCode import Button
import sys, time, os


pygame.init()
theme_music= pygame.mixer.Sound("JazzTheme.mp3")
pygame.mixer.music.load("JazzTheme.mp3")
pygame.mixer.music.set_volume(0.3)

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("LOGIC PUZZLE GAME")

#CONSTANTS 
BG = pygame.image.load("Background.jpg")  #BlueBackground
PUZZLE = pygame.image.load("puzzlebg.jpg")  #level1Background
LEVEL1 = pygame.image.load("level1.jpg")  #
LEVEL2 = pygame.image.load("level2.jpg")
LEVEL3 = pygame.image.load("level3.gif")            




#CURSOR
magcursor=pygame.image.load("mag_cursor.png").convert()

#FONT
base_font = pygame.font.SysFont('Arial',40)




clk=pygame.time.Clock()





def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)



def play():  #MainPlayFunction 
    answer = ""

    screen.blit(PUZZLE,(0, 0))
    

    answer_rect = pygame.Rect(550,500,140,32)
    colour = pygame.Color('lightskyblue3')

    

    def wrongAnswer():  #If the answer input is wrong
       
        while True:
            screen.fill('black')
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            A1 = Button(image=None, pos=(500, 550), 
                                text_input="TRY AGAIN", font=get_font(20), base_color="WHITE", hovering_color="BLUE")
            A1.changeColor(PLAY_MOUSE_POS)
            A1.update(screen)
            B1 = Button(image=None, pos=(770, 550), 
                                text_input="MAIN MENU", font=get_font(20), base_color="WHITE", hovering_color="BLUE")
            B1.changeColor(PLAY_MOUSE_POS)
            B1.update(screen)
            
            textLine1 = 'Your Answer is Incorrect!'
            text_surface = base_font.render(textLine1,True,(200,0,0))
            screen.blit(text_surface,(450,300))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if A1.checkForInput(PLAY_MOUSE_POS):
                        play()
                    if B1.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
            pygame.display.flip()
        


    def hint_phase():  #Hint screen for level1

        while True:

            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            screen.blit(BG, (0, 0))
            bravo = "Q. Which function is used to print an image/text to the screen:"
            hintquestion_surface= base_font.render(bravo,True,(255,255,255))
            screen.blit(hintquestion_surface,(200,150))

            A = Button(image=None, pos=(380, 310), 
                            text_input="A. surface.blit()", font=get_font(20), base_color="White", hovering_color="BLUE")
            A.changeColor(PLAY_MOUSE_POS)
            A.update(screen)

            B= Button(image=None, pos=(380, 350), 
                            text_input="B. surface.print()", font=get_font(20), base_color="White", hovering_color="BLUE")
            B.changeColor(PLAY_MOUSE_POS)
            B.update(screen)

            C = Button(image=None, pos=(380, 390), 
                            text_input="C. surface.display()", font=get_font(20), base_color="White", hovering_color="BLUE")
            C.changeColor(PLAY_MOUSE_POS)
            C.update(screen)

            D = Button(image=None, pos=(380, 430), 
                            text_input="D. surface.update() ", font=get_font(20), base_color="White", hovering_color="BLUE")
            D.changeColor(PLAY_MOUSE_POS)
            D.update(screen)
            
            E = Button(image=None, pos=(650, 600), 
                            text_input="BACK", font=get_font(20), base_color="White", hovering_color="BLUE")
            E.changeColor(PLAY_MOUSE_POS)
            E.update(screen)
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if A.checkForInput(PLAY_MOUSE_POS):
                            hint_surface= base_font.render(hint,True,(200,225,125))
                            screen.blit(hint_surface,(300,500))
                            pygame.display.flip()
                            clk.tick(1)
                            
                    


                    else:
                        incorrect = "PLEASE DOUBLE-CLICK THE CORRECT OPTION!"
                        message_surface = base_font.render(incorrect,True,(200,225,125))
                        screen.blit(message_surface,(300,620))
                        pygame.display.flip()
                        clk.tick(1)
                    if E.checkForInput(PLAY_MOUSE_POS):
                        play()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or pygame.K_KP_ENTER:
                        play()
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                
                        #level2
            pygame.display.update()


    def hint_phase2():   #hint screen for level2

        while True:

            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            screen.blit(BG, (0, 0))
            bravo = "Q. An array of pixels in the picture are stored in which of the following locations?"
            hint2 = "THE 'TEARS' BRING MONSOON"

            hintquestion_surface= base_font.render(bravo,True,(255,255,255))
            screen.blit(hintquestion_surface,(75,150))

            A = Button(image=None, pos=(650, 310), 
                            text_input="A. Frame buffer", font=get_font(20), base_color="White", hovering_color="BLUE")
            A.changeColor(PLAY_MOUSE_POS)
            A.update(screen)

            B= Button(image=None, pos=(650, 350), 
                            text_input="B. Processor", font=get_font(20), base_color="White", hovering_color="BLUE")
            B.changeColor(PLAY_MOUSE_POS)
            B.update(screen)

            C = Button(image=None, pos=(650, 390), 
                            text_input="C. Memory", font=get_font(20), base_color="White", hovering_color="BLUE")
            C.changeColor(PLAY_MOUSE_POS)
            C.update(screen)

            D = Button(image=None, pos=(650, 430), 
                            text_input="D. All of the above ", font=get_font(20), base_color="White", hovering_color="BLUE")
            D.changeColor(PLAY_MOUSE_POS)
            D.update(screen)
            
            E = Button(image=None, pos=(650, 600), 
                            text_input="BACK", font=get_font(20), base_color="White", hovering_color="BLUE")
            E.changeColor(PLAY_MOUSE_POS)
            E.update(screen)
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if C.checkForInput(PLAY_MOUSE_POS):
                            hint_surface= base_font.render(hint2,True,(200,225,125))
                            screen.blit(hint_surface,(200,600))
                            pygame.display.flip()
                            clk.tick(1)
                            
                    


                    else:
                        incorrect = "PLEASE DOUBLE-CLICK THE CORRECT OPTION!"
                        message_surface = base_font.render(incorrect,True,(200,225,125))
                        screen.blit(message_surface,(200,600))
                        pygame.display.flip()
                        clk.tick(1)
                    if E.checkForInput(PLAY_MOUSE_POS):
                        level2()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or pygame.K_KP_ENTER:
                        play()
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                
                        #level2
            pygame.display.update()

    def correctAnswer():  #if answer is correct for level1
            while True:

                PLAY_MOUSE = pygame.mouse.get_pos()
                screen.blit(BG, (0, 0))
                bravo = "Correct Answer! You have completed the level!"
                charlie= "Press enter key to continue"   #CongratsMesage
                text_surface= base_font.render(bravo,True,(255,255,255))
                screen.blit(text_surface,(325,300))
                text_surface2= base_font.render(charlie,True,(255,100,100))
                screen.blit (text_surface2,(450,400))


                CONTINUE2 = Button(image=None, pos=(640, 660), 
                            text_input="CONTINUE", font=get_font(20), base_color="White", hovering_color="BLUE")
                CONTINUE2.changeColor(PLAY_MOUSE)
                CONTINUE2.update(screen)


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if CONTINUE2.checkForInput(PLAY_MOUSE):
                            level2()
                            
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN or pygame.K_KP_ENTER:
                            level2()
                  
                pygame.display.flip()
                        
            

    hint = "HINT : RUN THE 'ENGINE' OF YOUR MIND...."
    
    #MAIN_PLAY_AREA

    def level2():
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(PUZZLE, (0,0))
        
        

        def checkAnswer2(text):  #checksAnswer for level2
            if text in ('Cloud','cloud','CLOUD','a cloud','A CLOUD','clouds','CLOUDS'):
                print("CORRECT ANSWER!") #level2
                level3()
            else:
                wrongAnswer()


        #Question and Answer Block
        

        #1st question

        answer = ""
        while True:

            PLAY_MOUSE_POS= pygame.mouse.get_pos()


            question = "Q. Solve the following riddle"   #1st question
            screen.blit(LEVEL2,(520,280))
            text_surface= base_font.render(question,True,(255,255,255))
            screen.blit(text_surface,(430,200))

            SUBMIT = Button(image=None, pos=(640, 660), 
                                text_input="SUBMIT", font=get_font(20), base_color="White", hovering_color="BLUE")
            SUBMIT.changeColor(PLAY_MOUSE_POS)
            SUBMIT.update(screen)

            HINT = Button(image=None, pos=(1180, 620), 
                                text_input="HINT", font=get_font(20), base_color="White", hovering_color="BLUE")
            HINT.changeColor(PLAY_MOUSE_POS)
            HINT.update(screen)



        
            
            PLAY_BACK = Button(image=None, pos=(140,620), 
                                text_input="MAIN MENU", font=get_font(20), base_color="White", hovering_color="BLUE")
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                #MAINMENU
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
                        #level2

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        answer = answer[0:-1]



                    else:
                        answer += event.unicode
                    
                        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :
                            #answer = answer[0:-1]
                            checkAnswer2(answer)
                        
                    screen.blit(PUZZLE,(0,0)) 

                    pygame.draw.rect(screen,colour,answer_rect,2)
                    
                    clk.tick(60)


                text_surface= base_font.render(answer,True,(255,255,255))
                screen.blit(text_surface,(answer_rect.x+7,answer_rect.y-7))
                    


                #SUBMIT_BUTTON

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SUBMIT.checkForInput(PLAY_MOUSE_POS):
                        checkAnswer2(answer)
                        #level2
                    
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if HINT.checkForInput(PLAY_MOUSE_POS):
                        hint_phase2()
                        
            pygame.display.flip()

    def level3():

         while True:
            screen.blit(LEVEL3,(0,0))
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            A1 = Button(image=None, pos=(500, 650), 
                                text_input="PLAY AGAIN", font=get_font(20), base_color="WHITE", hovering_color="BLUE")
            A1.changeColor(PLAY_MOUSE_POS)
            A1.update(screen)
            B1 = Button(image=None, pos=(770, 650), 
                                text_input="MAIN MENU", font=get_font(20), base_color="WHITE", hovering_color="BLUE")
            B1.changeColor(PLAY_MOUSE_POS)
            B1.update(screen)
            
            textLine1 = 'THIS GAME IS UNDER FURTHER DEVELOPMENT....'
            text_surface = base_font.render(textLine1,True,(255,0,0))
            screen.blit(text_surface,(290,100))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if A1.checkForInput(PLAY_MOUSE_POS):
                        play()
                    if B1.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
            pygame.display.flip()


    while True:
        pygame.mixer.music.stop()


        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        
        
    
        def checkAnswer1(text):
            if text in ('R','r','Reverse','reverse'):
                print("CORRECT ANSWER!") #level2
                correctAnswer()
            else:
                wrongAnswer()


        #Question Block
        question = "Q. What will replace the '?' in the image:"   #1st question
        screen.blit(LEVEL1,(480,250))
        text_surface= base_font.render(question,True,(255,255,255))
        screen.blit(text_surface,(350,200))


        #1st question
        screen.blit(LEVEL1,(480,250))
        

        #BUTTONS
        SUBMIT = Button(image=None, pos=(640, 660), 
                            text_input="SUBMIT", font=get_font(20), base_color="White", hovering_color="BLUE")
        SUBMIT.changeColor(PLAY_MOUSE_POS)
        SUBMIT.update(screen)

        HINT = Button(image=None, pos=(1180, 620), 
                            text_input="HINT", font=get_font(20), base_color="White", hovering_color="BLUE")
        HINT.changeColor(PLAY_MOUSE_POS)
        HINT.update(screen)

        
        PLAY_BACK = Button(image=None, pos=(140,620), 
                            text_input="MAIN MENU", font=get_font(20), base_color="White", hovering_color="BLUE")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        #eventLoops
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #MAINMENU
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                    #level2


            #typingAnswers
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    answer = answer[0:-1]   #backspace



                else:
                    answer += event.unicode
                
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER :     #submittingAnswer
                        answer = answer[0:-1]
                        checkAnswer1(answer)
                    
                screen.blit(PUZZLE,(0,0)) 

                pygame.draw.rect(screen,colour,answer_rect,2) 
                
                clk.tick(60)


                text_surface= base_font.render(answer,True,(255,255,255))
                screen.blit(text_surface,(answer_rect.x+7,answer_rect.y-7))  #textBoxoutline
                

            

            #SUBMIT_BUTTON

            if event.type == pygame.MOUSEBUTTONDOWN:
                if SUBMIT.checkForInput(PLAY_MOUSE_POS):
                    checkAnswer1(answer)
                    #level2
                
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HINT.checkForInput(PLAY_MOUSE_POS):
                    hint_phase()
                    
        pygame.display.flip()
    
    
def options():
    pygame.mixer.music.play(-1)
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="BLUE")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    pygame.mixer.music.play(-1)
    pygame.mouse.set_visible(True)
    while True:

        screen.blit(BG, (0, 0))
        
        

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(70).render("LOGIC PUZZLE GAME", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for buttonCode in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            buttonCode.changeColor(MENU_MOUSE_POS)
            buttonCode.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()

