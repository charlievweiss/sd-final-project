# Heck Decks
## Andrew Holmes, Brennan VandenHoek, Arpan Rau, Charlie Weiss

##Build using SolidPython, Flask, and Openscad

# Description
Hex Decks is a python program that generates custom skateboard decks tailored to you and your riding style. Hex Decks is based off of previous research that was done at Olin college characterizing the effect that a change in core geometry has on the stiffness of a composite skateboard deck. Hex Decks takes data about the rider's weight and stiffness preferences through a web interface and generates a .DXF cut file that can be used to make a skateboard with the specified stiffness characteristics. 

Learn more about the project at our [website](https://sites.google.com/view/hexdeck)

# Getting started
Hexdecks supports UNIX environments and was built in and for Ubuntu Linux. Our installation instructions assume you already have [Python 2.7](https://www.python.org/download/releases/2.7/) and [Git](https://git-scm.com/downloads).
#### Here's how to install it:
* With console commands

1. Install [Flask](http://flask.pocoo.org/) 
  * $sudo pip install flask 
2. Install [OpenScad](http://www.openscad.org/) 
  * $ sudo add-apt-repository ppa:openscad/releases    
  * $ sudo apt-get update 
  * $ sudo apt-get install openscad 
3. Install [SolidPython](https://github.com/SolidCode/SolidPython#installing-solidpython) via the download method (PypI will install an old version that is not compatible with HexDecks) 
  * $git clone https://github.com/SolidCode/SolidPython.git  
  * $sudo python setup.py install 
4. Clone our [repository](https://github.com/charlievweiss/sd-final-project) to the directory of your choice 
  * $git clone https://github.com/charlievweiss/sd-final-project.git 
5. Launch main.py to start the backend and [click here](http://127.0.0.1:5000/) to make a sick deck! 
  * $python main.py 

# License

Project under a CC license. See the license.txt file for more info



  
