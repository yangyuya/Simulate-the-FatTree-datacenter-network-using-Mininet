# Simulate-the-FatTree-datacenter-network-using-Mininet

experiment1:
远程登陆打开两个mininet窗口，先在窗口1输入下面的命令：
cd pox
python pox.py forwarding.l2_learning openflow.discovery openflow.spanning_tree --no-flood --hold-down openflow.keepalive openflow.of_01
再在窗口2运行fattree.py：
sudo python fattree.py

断开三条链路进行测试：
保持窗口1不变，在窗口2关掉原来的程序，
exit
修改fattree.py程序，将下面三条语句前的注释去掉，然后重新运行：
#    net.configLinkStatus('s3', 's14', 'down')
#    net.configLinkStatus('s24', 's21', 'down')
#    net.configLinkStatus('s11', 's13', 'down')

experiment2:
打开一个mininet窗口，在窗口中直接运行myfattree.py：
sudo python myfattree.py

