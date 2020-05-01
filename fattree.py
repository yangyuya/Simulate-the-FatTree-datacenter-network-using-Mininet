 #!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernetSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myFattree():
    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')
    
    info( '*** Adding controller\n')

    c0=net.addController(name='c0',
                         controller=RemoteController,
                         protocol='tcp',
                         port=6633)

    info(' *** Add switches\n')
    ''''
    一共有四组交换机，一共20个，每组的排序按照从下到上从左到右
    ''''
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch)
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch)
    s14 = net.addSwitch('s14', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s21 = net.addSwitch('s21', cls=OVSKernelSwitch)
    s22 = net.addSwitch('s22', cls=OVSKernelSwitch)
    s23 = net.addSwitch('s23', cls=OVSKernelSwitch)
    s24 = net.addSwitch('s24', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s31 = net.addSwitch('s31', cls=OVSKernelSwitch)
    s32 = net.addSwitch('s32', cls=OVSKernelSwitch)
    s33 = net.addSwitch('s33', cls=OVSKernelSwitch)
    s34 = net.addSwitch('s34', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s41 = net.addSwitch('s41', cls=OVSKernelSwitch)
    s42 = net.addSwitch('s42', cls=OVSKernelSwitch)
    s43 = net.addSwitch('s43', cls=OVSKernelSwitch)
    s44 = net.addSwitch('s44', cls=OVSKernelSwitch)

    info(' *** Add hosts\n')
    ''''
    一共16个主机
    ''''
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.2',defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.3',defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.1.2',defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.1.3',defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.1.0.2',defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.1.0.3',defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.1.1.2',defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.1.1.3',defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.2.0.2',defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.2.0.3',defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.2.1.2',defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.2.1.3',defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.3.0.2',defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.3.0.3',defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.3.1.2',defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.3.1.3',defaultRoute=None)

    info(' *** Add links\n')
    ''''
    第一层交换机与第二层的连接
    ''''
    net.addLink(s1,s13)
    net.addLink(s1,s23)
    net.addLink(s1,s33)
    net.addLink(s1,s43)
    net.addLink(s2,s13)
    net.addLink(s2,s23)
    net.addLink(s2,s33)
    net.addLink(s2,s43)
    net.addLink(s3,s14)
    net.addLink(s3,s24)
    net.addLink(s3,s34)
    net.addLink(s3,s44)
    net.addLink(s4,s14)
    net.addLink(s4,s24)
    net.addLink(s4,s34)
    net.addLink(s4,s44)
    ''''
    第二层之间的连接
    ''''
    net.addLink(s11,s13)
    net.addLink(s11,s14)
    net.addLink(s12,s13)
    net.addLink(s12,s14)
    net.addLink(s21,s23)
    net.addLink(s21,s24)
    net.addLink(s22,s23)
    net.addLink(s22,s24)
    net.addLink(s31,s33)
    net.addLink(s31,s34)
    net.addLink(s32,s33)
    net.addLink(s32,s34)
    net.addLink(s41,s43)
    net.addLink(s41,s44)
    net.addLink(s42,s43)
    net.addLink(s42,s44)
    ''''
    第二层和第三层之间的连接
    ''''
    net.addLink(s11,h1)
    net.addLink(s11,h2)
    net.addLink(s12,h3)
    net.addLink(s12,h4)
    net.addLink(s21,h5)
    net.addLink(s21,h6)
    net.addLink(s22,h7)
    net.addLink(s22,h8)
    net.addLink(s31,h9)
    net.addLink(s31,h10)
    net.addLink(s32,h11)
    net.addLink(s32,h12)
    net.addLink(s41,h13)
    net.addLink(s41,h14)
    net.addLink(s42,h15)
    net.addLink(s42,h16)

    info(' *** Starting network\n')
    net.build()
    info(' *** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info(' *** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s11').start([c0])
    net.get('s12').start([c0])
    net.get('s13').start([c0])
    net.get('s14').start([c0])
    net.get('s2').start([c0])
    net.get('s21').start([c0])
    net.get('s22').start([c0])
    net.get('s23').start([c0])
    net.get('s24').start([c0])
    net.get('s3').start([c0])
    net.get('s31').start([c0])
    net.get('s32').start([c0])
    net.get('s33').start([c0])
    net.get('s34').start([c0])
    net.get('s4').start([c0])
    net.get('s41').start([c0])
    net.get('s42').start([c0])
    net.get('s43').start([c0])
    net.get('s44').start([c0])
    

    info(' *** Post configure switches and hosts\n')
#    net.configLinkStatus('s3', 's14', 'down')
#    net.configLinkStatus('s24', 's21', 'down')
#    net.configLinkStatus('s11', 's13', 'down')    

    CIL(net)
    net.stop()

if __name__=='__main__':
    setLogLevel('info')
    myFattree()
    
    
    
    


    
