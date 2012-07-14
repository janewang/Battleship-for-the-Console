from pprint import pprint
import random
import sys

def main():
    
    aircraft_carrier = []
    battle_ship = []
    submarine = []
    destroyer = []
    patrol_boat = []
    
    aircraft_carrier_status = 0
    battle_ship_status = 0
    submarine_status = 0
    destroyer_status = 0
    patrol_boat_status = 0
  
    def initialize():
        board  = []      
        for i in xrange(10):
            board.append([])
            for j in xrange(10):
                board[i].append(' ')
        return board


    def fireshot(aircraft_carrier_status, battle_ship_status, submarine_status, destroyer_status, patrol_boat_status):
        fire = input('You may fire when ready (x, y): ')
        x = fire[0]
        y = fire[1]
        
        if board[x][y] == ' ':
            print '\033[91m' + 'Miss!' + '\033[0m'
        
        board[x][y] = '0'
        showboard[x][y] = '0'
        aircraft_carrier_status, battle_ship_status, submarine_status, destroyer_status, patrol_boat_status = gamestate(showboard, board, x, y, aircraft_carrier_status, battle_ship_status, submarine_status, destroyer_status, patrol_boat_status)
        # print below the hidden board
        # pprint(board)
        # print below the play board
        print " "
        pprint(showboard)
        fireshot(aircraft_carrier_status, battle_ship_status, submarine_status, destroyer_status, patrol_boat_status)
        
    
    def find_open_spot(row, row_number, required_number, num_repeats, stop_after_match=True):
        i = random.randrange(0, 9 - num_repeats)
        while i < len(row):                   
            if [required_number]*num_repeats == row[i:i + num_repeats]:
                row[i:i+num_repeats] = ['x']*num_repeats                  
  
                if num_repeats == 5:
                    for coords in xrange(5):
                        aircraft_carrier.append([row_number, i+coords])
                        
                elif num_repeats == 4:
                    for coords in xrange(4):
                        battle_ship.append([row_number, i+coords])

                elif num_repeats == 3:
                     if len(submarine) < 3:
                          for coords in xrange(3):
                              submarine.append([row_number, i+coords])
                     else:
                          for coords in xrange(3):
                              destroyer.append([row_number, i+coords])

                elif num_repeats == 2:
                    for coords in xrange(2):
                        patrol_boat.append([row_number, i+coords])
              
                i += num_repeats                                                  
                if stop_after_match:
                    break
            else:
                i += 1
          
        return row

    
    def generate_ship(board, space, number):
        row_number = random.randrange(0, 9)    
        row = board[row_number]
        x = find_open_spot(row, row_number, space, number)
        board[row_number] = x                              
        return board        

        
    def transform_board(board, shiptype):
        a = board
        board = initialize()
        for i in xrange(10):
            for j in xrange(10):
                board[j][i] = a[i][j]       

        if shiptype > 0 and shiptype < 5:
              for num in xrange(5):
                  aircraft_carrier[num].reverse()
        
        if shiptype > 1 and shiptype < 5:
              for num in xrange(4):
                  battle_ship[num].reverse()
        
        if shiptype > 2 and shiptype < 5:
              for num in xrange(3):
                  submarine[num].reverse()
        
        if shiptype > 3 and shiptype < 5:
              for num in xrange(3):
                  destroyer[num].reverse()
      
        return board
  

    
    def gamestate(showboard, board, x, y, aircraft_carrier_status, battle_ship_status, submarine_status, destroyer_status, patrol_boat_status):
        
        if [x] + [y] in aircraft_carrier:
              aircraft_carrier_status += 1
              showboard[x][y] = 'x'
              print '\033[91m' + 'Aircraft carrier has been hit!' + '\033[0m'
              if aircraft_carrier_status == 5:
                  print '\033[91m' + 'Aircraft carrier has been sank!' + '\033[0m'
      
        elif [x] + [y] in battle_ship:            
              battle_ship_status += 1
              showboard[x][y] = 'x'
              print '\033[91m' + 'Battle ship has been hit!' + '\033[0m'
              if battle_ship_status == 4:
                  print '\033[91m' +  'Battle ship has been sank!' + '\033[0m'
  
        elif [x] + [y] in submarine:
              submarine_status += 1
              showboard[x][y] = 'x'
              print '\033[91m' +  'Submarine has been hit!' + '\033[0m'
              if submarine_status == 3:
                  print '\033[91m' +  'Submarine has been sank!' + '\033[0m'
               
        elif [x] + [y] in destroyer:
              destroyer_status += 1
              showboard[x][y] = 'x'
              print '\033[91m' + 'Destroyer has been hit!' + '\033[0m'
              if destroyer_status == 3:
                  print '\033[91m' +  'Destroyer has been sank!' + '\033[0m'
                  
        elif [x] + [y] in patrol_boat:
              patrol_boat_status += 1
              showboard[x][y] = 'x'
              print '\033[91m' +'Patrol boat has been hit!' + '\033[0m'
              if patrol_boat_status == 2:
                  print '\033[91m' +'Patrol boat has been sank!' + '\033[0m'
        
        counter = 0
        for i in xrange(10):
            for j in xrange(10):
                  if board[i][j] == 'x':
                      counter+=1
        if counter == 0:
            print '\033[91m' + 'Game over!' + '\033[0m'
            sys.exit(0)
        
        return aircraft_carrier_status, battle_ship_status, submarine_status, destroyer_status, patrol_boat_status
    
  
    # starting the game
    ships = [5, 4, 3, 3, 2]
    board = initialize()
        
    for i in xrange(5):
        if ( int(round(random.random())) == 1):
            board = transform_board(board, i)            
        board = generate_ship(board, ' ', ships[i])
    
    # print the hidden board
    # print 'aircraft carrier', aircraft_carrier
    # print 'battle ship', battle_ship
    # print 'submarine', submarine
    # print 'destroyer', destroyer
    # print 'patrol boat', patrol_boat
    # pprint(board)
    # print " "
    
    #print the play board
    showboard = initialize()
    print " "
    print "Welcome to Battleship!"
    pprint(showboard)
    fireshot(aircraft_carrier_status, battle_ship_status, submarine_status, destroyer_status, patrol_boat_status)
   
    
if __name__ == "__main__":
    main()