import sys
import pygame as pg

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg") #練習１
    bg_img2 = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img2, True, False) #演習２
    # bg_imgs = [bg_img, bg_img2]

    kk_img = pg.image.load("ex01/fig/3.png") #練習２
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs1 = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)] #練習３


    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = (tmr%3200) #練習４
        screen.blit(bg_img, [-x, 0]) 
        screen.blit(bg_img2, [1600-x, 0]) #練習６
        screen.blit(bg_img, [3200-x, 0]) #演習２


        # screen.blit(bg_imgs[tmr%800], [x, 0])
        screen.blit(kk_imgs1[tmr%2], [300, 200]) #練習５
        pg.display.update()
        tmr += 1        
        clock.tick(100) #演習１


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()