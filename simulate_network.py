# 1. Create a Simulator Object 
set ns [new Simulator] 

# 2. Open the NAM (Network Animator) trace file 
set nf [open out.nam w]
$ns namtrace-all $nf 

# 3. Define a 'finish' procedure to close files and launch NAM 
proc finish {} { 
global ns nf 
$ns flush-trace 
close $nf 
exec nam out.nam & 
exit 0 
} 

# 4. Create two nodes 
set n0 [$ns node] 
set n1 [$ns node] 

# 5. Create a Duplex Link between nodes 
# Syntax: $ns duplex-link <node1> <node2> <bandwidth> <delay> <queue_type> 
$ns duplex-link $n0 $n1 1Mb 10ms DropTail 

# 6. Setup a UDP Connection 
set udp [new Agent/UDP] 
$ns attach-agent $n0 $udp 
set null [new Agent/Null] 
$ns attach-agent $n1 $null 
# Connect the two agents 
$ns connect $udp $null 

# 7. Setup a Traffic Source (CBR - Constant Bit Rate) 
set cbr [new Application/Traffic/CBR] 
$cbr attach-agent $udp 
$cbr set packetSize_ 500 
$cbr set interval_ 0.005 

# 8. Schedule Events 
$ns at 0.5 "$cbr start" 
$ns at 4.5 "$cbr stop" 
$ns at 5.0 "finish" 

# 9. Run the simulation 
$ns run