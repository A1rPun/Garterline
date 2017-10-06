from garterline import GarterLine

def haxxor():
    delimiter = "]─["
    haxx = GarterLine()
    haxx.color("196", "5", "38")
    haxx.text("┌─[")
    haxx.color("28", "5", "38")
    haxx.escape("username")
    haxx.color("196", "5", "38")
    haxx.text(delimiter)
    haxx.color("10", "5", "38")
    haxx.escape("fullhostname")
    haxx.color("196", "5", "38")
    haxx.text(delimiter)
    haxx.color("41", "5", "38")
    haxx.escape("directory")
    haxx.color("196", "5", "38")
    haxx.text("]")
    haxx.escape("newline")
    haxx.text("└─$")
    haxx.color("10", "5", "38")
    return haxx

def arrows():
    arrow = ">"
    arr = GarterLine()
    arr.color("10", "5", "38")    
    arr.text(arrow)
    arr.color("41", "5", "38")
    arr.text(arrow)
    arr.color("28", "5", "38")
    arr.text(arrow)
    arr.text(" ")    
    arr.escape("directory")
    arr.escape("newline")
    arr.color("28", "5", "38")
    arr.text(arrow)
    arr.color("41", "5", "38")
    arr.text(arrow)
    arr.color("10", "5", "38")
    arr.text(arrow)
    arr.text(" ")    
    return arr

def garter():
    delimiter = "▶"
    gar = GarterLine()
    gar.color("black", "blue")
    gar.text(" ")
    gar.escape("username")
    gar.text(" ")
    gar.color("blue", "lightblue")    
    gar.text(delimiter)
    gar.color("black", "lightblue")
    gar.text(" ")
    gar.escape("fullhostname")
    gar.text(" ")
    gar.color("lightblue", "cyan")
    gar.text(delimiter)
    gar.color("black", "cyan")
    gar.text(" ")
    gar.escape("directory")
    gar.text(" ")
    gar.color("cyan", "lightcyan")
    gar.text(delimiter)
    gar.color("black", "lightcyan")
    gar.text(" ")
    gar.escape("number")
    gar.text(" ")
    gar.color("lightcyan")    
    gar.text(delimiter)
    gar.escape("newline")
    gar.color("black", "blue")
    gar.text("$")
    gar.color("blue")    
    gar.text(delimiter)
    gar.color("lightcyan")
    return gar

def mono():
    delimiter = "░"
    mon = GarterLine()
    mon.color("black", "white")
    mon.escape("number")
    mon.color("white", "lightgray")
    mon.text(delimiter)
    mon.color("black", "lightgray")
    mon.escape("username")
    mon.color("lightgray", "gray")
    mon.text(delimiter)
    mon.color("white", "gray")
    mon.escape("fullhostname")
    mon.color("gray", "black")
    mon.text(delimiter)
    mon.color("white", "black")
    mon.escape("directory")
    mon.escape("newline")
    mon.text("$")
    return mon

command = "bash command"
print(haxxor(), command)
print(arrows(), command)
print(garter(), command)
print(mono(), command)
print(GarterLine().color())
