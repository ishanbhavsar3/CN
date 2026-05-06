# Create Simulator object
set ns [new Simulator]
# Define colors
$ns color 1 Blue
$ns color 2 Red
# Open NAM trace file
set nf [open out.nam w]
$ns namtrace-all $nf

# Finish procedure
proc finish {} {
global ns nf
$ns flush-trace
close $nf
exec nam out.nam &
exit 0
}
# Create 6 nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
# ----------- FULL MESH CONNECTIONS -----------
$ns duplex-link $n0 $n1 2Mb 10ms DropTail
$ns duplex-link $n0 $n2 2Mb 10ms DropTail
$ns duplex-link $n0 $n3 2Mb 10ms DropTail
$ns duplex-link $n0 $n4 2Mb 10ms DropTail
$ns duplex-link $n0 $n5 2Mb 10ms DropTail
$ns duplex-link $n1 $n2 2Mb 10ms DropTail
$ns duplex-link $n1 $n3 2Mb 10ms DropTail
$ns duplex-link $n1 $n4 2Mb 10ms DropTail
$ns duplex-link $n1 $n5 2Mb 10ms DropTail
$ns duplex-link $n2 $n3 2Mb 10ms DropTail
$ns duplex-link $n2 $n4 2Mb 10ms DropTail
$ns duplex-link $n2 $n5 2Mb 10ms DropTail
$ns duplex-link $n3 $n4 2Mb 10ms DropTail
$ns duplex-link $n3 $n5 2Mb 10ms DropTail
$ns duplex-link $n4 $n5 2Mb 10ms DropTail
# -------------------------------------------
# Set queue limit (example)

$ns queue-limit $n2 $n3 10
# ---------------- TCP CONNECTION ----------------
set tcp [new Agent/TCP]
$tcp set class_ 2
$ns attach-agent $n0 $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n5 $sink
$ns connect $tcp $sink
$tcp set fid_ 1
# FTP over TCP
set ftp [new Application/FTP]
$ftp attach-agent $tcp
# ---------------- UDP CONNECTION ----------------
set udp [new Agent/UDP]
$ns attach-agent $n1 $udp
set null [new Agent/Null]
$ns attach-agent $n4 $null
$ns connect $udp $null
$udp set fid_ 2
# CBR over UDP
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set packet_size_ 1000
$cbr set rate_ 1mb
# Schedule events
$ns at 0.1 "$cbr start"
$ns at 1.0 "$ftp start"
$ns at 4.0 "$ftp stop"
$ns at 4.5 "$cbr stop"
# End simulation

$ns at 5.0 "finish"
# Run simulation
$ns run