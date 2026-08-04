"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Theme

Description: Central stylesheet for the Lumora AI Desktop Application.Inspired by the official Lumora project poster.

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
    font-family:"Segoe UI";
    font-size:15px;
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

    border-right:1px solid #2D3E63;
}


/* ============================================================
                        AVATAR PANEL
============================================================ */

#avatarPanel{

    background:qlineargradient(
        x1:0,
        y1:0,
        x2:0,
        y2:1,
        stop:0 #0A1020,
        stop:1 #171F38
    );

    border-left:1px solid #2D3E63;
}


/* ============================================================
                        TITLES
============================================================ */

#title{

    color:#F6C667;

    font-size:24px;

    font-weight:700;
}


#subtitle{

    color:#C7D2E5;

    font-size:13px;
}


/* ============================================================
                        LABELS
============================================================ */

QLabel{

    color:white;

    background:transparent;
}


/* ============================================================
                        BUTTONS
============================================================ */

QPushButton{

    background:#222F46;

    border:1px solid #39517D;

    border-radius:16px;

    padding:12px;

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
                    MESSAGE INPUT
============================================================ */

QLineEdit{

    background:#131C2F;

    border:2px solid #39517D;

    border-radius:18px;

    padding:12px;

    color:white;

    font-size:15px;
}


QLineEdit:focus{

    border:2px solid #8C6CFF;
}


/* ============================================================
                    SEND BUTTON
============================================================ */

#sendButton{

    background:qlineargradient(
        x1:0,
        y1:0,
        x2:1,
        y2:1,
        stop:0 #6C5BFF,
        stop:1 #A45DFF
    );

    border:none;

    border-radius:18px;

    color:white;

    font-weight:bold;

    font-size:18px;
}


#sendButton:hover{

    background:qlineargradient(
        x1:0,
        y1:0,
        x2:1,
        y2:1,
        stop:0 #816DFF,
        stop:1 #B576FF
    );
}


/* ============================================================
                        CHAT AREA
============================================================ */

QScrollArea{

    background:#0D1526;

    border:1px solid #2C3E63;

    border-radius:20px;
}


QScrollArea QWidget{

    background:transparent;
}


/* ============================================================
                    USER MESSAGE
============================================================ */

#userBubble{

    background:qlineargradient(
        x1:0,
        y1:0,
        x2:1,
        y2:0,
        stop:0 #6958FF,
        stop:1 #9A5EFF
    );

    color:white;

    border-radius:22px;

    padding:16px;
}


/* ============================================================
                    LUMORA MESSAGE
============================================================ */

#lumoraBubble{

    background:#222D43;

    border:1px solid #3A5280;

    color:white;

    border-radius:22px;

    padding:16px;
}


/* ============================================================
                    SCROLLBAR
============================================================ */

QScrollBar:vertical{

    background:#131C2F;

    width:12px;

    border:none;
}


QScrollBar::handle:vertical{

    background:#7A5AF8;

    border-radius:6px;
}


QScrollBar::handle:vertical:hover{

    background:#A285FF;
}


QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical{

    height:0px;
}

/* ============================================================
                    TYPING INDICATOR
============================================================ */

#typingIndicator{

    color:#67D7F5;

    font-size:14px;

    font-style:italic;

    padding:10px;
}

"""