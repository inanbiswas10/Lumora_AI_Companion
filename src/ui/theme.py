"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Theme

Description: Central stylesheet for Lumora AI Desktop. Inspired by the official Lumora project poster.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""


LUMORA_THEME = """

/* ============================================================
                        MAIN WINDOW
============================================================ */

QMainWindow{
    background:qlineargradient(
        x1:0,y1:0,
        x2:0,y2:1,
        stop:0 #07111E,
        stop:0.35 #111B33,
        stop:0.70 #20173B,
        stop:1 #0B1020
    );
}


/* ============================================================
                        GENERAL
============================================================ */

QWidget{
    background:transparent;
    color:white;
    font-size:15px;
    font-family:Segoe UI;
}


/* ============================================================
                        SIDEBAR
============================================================ */

#sidebar{

    background:qlineargradient(
        x1:0,y1:0,
        x2:0,y2:1,
        stop:0 #0A1020,
        stop:1 #171F38
    );

    border-right:1px solid #26365A;
}


QLabel{

    color:white;
}


QPushButton{

    background:#232E43;

    border:1px solid #32486D;

    border-radius:16px;

    padding:14px;

    color:white;

    font-size:15px;
}


QPushButton:hover{

    background:#314364;

    border:1px solid #7A5AF8;
}


QPushButton:pressed{

    background:#7A5AF8;
}


/* ============================================================
                        CHAT AREA
============================================================ */

QScrollArea{

    background:#0C1223;

    border:1px solid #26385A;

    border-radius:20px;
}


QTextEdit{

    background:#0C1223;

    border:none;

    color:white;

    selection-background-color:#7A5AF8;
}


/* ============================================================
                    MESSAGE INPUT
============================================================ */

QLineEdit{

    background:#141D31;

    border:2px solid #32486D;

    border-radius:18px;

    padding:12px;

    color:white;

    font-size:15px;
}


QLineEdit:focus{

    border:2px solid #7A5AF8;
}


/* ============================================================
                    SEND BUTTON
============================================================ */

#sendButton{

    background:qlineargradient(
        x1:0,y1:0,
        x2:1,y2:1,
        stop:0 #6E5BFF,
        stop:1 #9B5CFF
    );

    border:none;

    border-radius:18px;

    color:white;

    font-size:16px;

    font-weight:bold;
}


#sendButton:hover{

    background:qlineargradient(
        x1:0,y1:0,
        x2:1,y2:1,
        stop:0 #816DFF,
        stop:1 #AE76FF
    );
}


/* ============================================================
                    USER MESSAGE
============================================================ */

#userBubble{

    background:qlineargradient(
        x1:0,y1:0,
        x2:1,y2:0,
        stop:0 #6B5CFF,
        stop:1 #9B63FF
    );

    border-radius:22px;

    padding:18px;

    color:white;
}


/* ============================================================
                    LUMORA MESSAGE
============================================================ */

#lumoraBubble{

    background:#232C41;

    border:1px solid #344C77;

    border-radius:22px;

    padding:18px;

    color:white;
}


/* ============================================================
                    SCROLLBAR
============================================================ */

QScrollBar:vertical{

    background:#141B2E;

    width:12px;

    border:none;
}


QScrollBar::handle:vertical{

    background:#7A5AF8;

    border-radius:6px;
}


QScrollBar::handle:vertical:hover{

    background:#9D7CFF;
}


QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical{

    height:0;
}


/* ============================================================
                    STATUS PANEL
============================================================ */

#avatarPanel{

    background:qlineargradient(
        x1:0,y1:0,
        x2:0,y2:1,
        stop:0 #0A1020,
        stop:1 #171F38
    );

    border-left:1px solid #26365A;
}


/* ============================================================
                    HEADINGS
============================================================ */

#title{

    color:#F6C667;

    font-size:24px;

    font-weight:bold;
}


#subtitle{

    color:#C7D2E5;

    font-size:13px;
}

"""