"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        leftHost = self.addHost( 'h1' , ip='10.0.3.2')
	middleHost = self.addHost( 'h2' , ip='10.0.3.3')
        rightHost = self.addHost( 'h3' , ip='10.0.3.4')
        mainSwitch = self.addSwitch( 's1' )

        # Add links
        self.addLink( leftHost, mainSwitch , 1 , 1 )
        self.addLink( middleHost, mainSwitch , 1 , 2 )
        self.addLink( rightHost, mainSwitch , 1 , 3 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
