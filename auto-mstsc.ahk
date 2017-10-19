^j::
    Run, mstsc.exe
    Sleep, 500
    Send, !o
    Sleep, 200
    Send, ^{TAB}
    Sleep, 200
    Send, {end}
    Loop, 3
    {
        Sleep, 200
        Send, {left}
    }
    Send, {return}
Return