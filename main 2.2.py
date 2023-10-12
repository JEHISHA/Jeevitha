''' Implement a class called player that represents a cricket play. Th player class should have a
method called play() which prints "The players is playing cricket.Deriver a two classes, Batsman and
Bowler, from the player class.override the play () method in each derived class to print "The batsman
is batting " and "The blower is blowing ", respectively.write a program to create subjects or both the
Batsman and Bowler classes and call tha play() method for each object.'''


# Define the base class player
class player:
  def play(self):
    print("The player is playing cricket.")

# Define the derived class Batsman
class batsman (player):
      def play (self):
        print("The Batsman is batting.")

# Define the derived class Bowler
class bowler (player):
      def play(self):
          print("The Bowler is bowling.")
        
# create object of Batsman and Bowler classes
Batsman = batsman()
Bowler = bowler()

# call the play() method for each object
Batsman.play()
Bowler.play()