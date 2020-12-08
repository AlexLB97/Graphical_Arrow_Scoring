#Pseudocode
#initiate graphics window
    #window is 500 x 1000
    #window name is Target Plot
#draw a target of predetermined size
#create a button function that will zoom in 
#create a function that allows you to plot a predetermined number of arrows
#create another function that allows the user to plot any number of arrows
#create a function that lists the score for each arrow plotted
#return the end score at the bottom, and keep track of running score

#main()
#initiate list for arrow values
#ask user if they would like a structured or unstructured round
#if structured
    #initiate structuredRound
        #ask user how many arrows per end they would like to shoot
        #ask user how many ends they would like to shoot
        #return both inputs to respective variables
        #initiate graphics window
            #set size to 500x1000 and name to Target Plot
            #set coordinates to 
from graphics import *


    

def scoreArrow(arrow_position, target_window, score_list, value_X, value_Y):
    ring_radius_list = [1,2,3,4,5,6,7,8,9,10,20]
    ring_score_list =[10,9,8,7,6,5,4,3,2,1,0]
    ring_index = 0
    center_from_center = ((abs(arrow_position.getX())**2) + (abs(arrow_position.getY())**2))**(1/2)
    edge_from_center = center_from_center - 0.17
    for ring in ring_radius_list:
        if edge_from_center < ring:
            arrow_value = ring_score_list[ring_index]
            score_list.append(arrow_value)
            value_text = Text(Point(value_X, value_Y), arrow_value)
            value_text.draw(target_window)
            return score_list, value_X
        else:
            ring_index += 1
            

def plotArrows(arrow_list, number_arrows, score_list, value_X, value_Y):
    target_window = createWindow()
    drawTarget(target_window)
    for i in range(number_arrows):
            arrow_position = target_window.getMouse()
            arrow_list.append(arrow_position)
            arrow = Circle(arrow_position, 0.17)
            arrow.draw(target_window)
            score_list, value_X = scoreArrow(arrow_position, target_window, score_list, value_X + 1, value_Y)
    target_window.getKey()
    target_window.close()
    return arrow_list, score_list
           

def plotFirstEnd(target_window, number_arrows, number_ends):
    arrow_list = []
    score_list = []
    value_X = -5
    value_Y = -12
    for j in range(number_arrows):
        arrow_position = target_window.getMouse()
        arrow_list.append(arrow_position)
        arrow = Circle(arrow_position, 0.17)
        arrow.draw(target_window)
        score_list, value_X = scoreArrow(arrow_position, target_window, score_list, value_X+1, value_Y)
    target_window.getKey()
    target_window.close()
    value_X = -5
    for i in range(number_ends - 1):
        arrow_list, score_list = plotArrows(arrow_list, number_arrows, score_list, value_X, value_Y)
    return arrow_list, score_list

def plotAllArrows(arrow_list, score_list):
    target_window = createWindow()
    drawTarget(target_window)
    for point in arrow_list:
        arrow = Circle(point, 0.17)
        arrow.draw(target_window)
    score = sum(score_list)
    score_text = Text(Point(0, -12), score)
    score_text.draw(target_window)
    
def checkClick(target_window):
    click_point = target_window.getMouse()
    if 3 <= click_point.getX() <= 6 and -12.5 <= click_point.getY() <= -11.5:
        return True
    else:
        return checkClick(target_window)

        
def getArrows(target_window):
    arrow_entry = Text(Point(-4.5,-12),"Enter the number of arrows you will shoot per end:")
    arrow_entry.draw(target_window)
    number_arrows_entry = Entry(Point(1, -12), 2)
    number_arrows_entry.draw(target_window)
    enter_button = Rectangle(Point(3,-12.5), Point(6, -11.5))
    enter_button.setFill('green')
    enter_button.draw(target_window)
    button_clicked = checkClick(target_window)
    number_arrows = int(number_arrows_entry.getText())
    arrow_entry.undraw()
    number_arrows_entry.undraw()
    enter_button.undraw()
    return number_arrows
    
        

def getEnds(target_window):
    end_entry = Text(Point(-4.5,-12), "Enter the number of ends you will shoot:")
    end_entry.draw(target_window)
    number_ends_entry = Entry(Point(1,-12), 2)
    number_ends_entry.draw(target_window)
    enter_button = Rectangle(Point(3,-12.5), Point(6, -11.5))
    enter_button.setFill('green')
    enter_button.draw(target_window)
    button_clicked = checkClick(target_window)
    number_ends = int(number_ends_entry.getText())
    end_entry.undraw()
    number_ends_entry.undraw()
    enter_button.undraw()
    return number_ends


def drawTarget(target_window):
    radius_increment = 0
    ring_count = 1
    colors =['white','black','blue','red','yellow']
    color_index = 0
    for i in range(10):
        target_ring = Circle(Point(0, 0), 10 - radius_increment)
        target_ring.draw(target_window)
        target_ring.setFill(colors[color_index])
        radius_increment += 1
        color_index = ring_count // 2
        if ring_count == 4:
            target_ring.setOutline('white')
            ring_count += 1
        else:
            ring_count += 1
    to_continue = Text(Point(0, -17), 'Press any key to continue')
    to_continue.draw(target_window)
            

def createWindow():
    target_window = GraphWin('Target Plot', 800, (800 * (700/500)))
    target_window.setCoords(-10.0, -18.0, 10.0, 10.0)
    return target_window

def main():
    target_window = createWindow()
    drawTarget(target_window)
    number_arrows = getArrows(target_window)
    number_ends = getEnds(target_window)
    arrow_list, score_list = plotFirstEnd(target_window, number_arrows, number_ends)
    plotAllArrows(arrow_list, score_list)
main()
