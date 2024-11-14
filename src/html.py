
# ==================================================================================================

def html(text):
    """
    HTML tag.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text.
    """

    return f'<html>{text}</html>'

# --------------------------------------------------------------------------------------------------

def head(text):
    """
    HEAD tag.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text.
    """

    return f'<head>{text}</head>'

# --------------------------------------------------------------------------------------------------

def title(text):
    """
    TITLE tag.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text.
    """

    return f'<title>{text}</title>'

# --------------------------------------------------------------------------------------------------

def body(text):
    """
    BODY tag.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text.
    """

    return f'<body>{text}</body>'

# --------------------------------------------------------------------------------------------------

def table(text, border='1'):
    """
    TABLE tag.

    Parameters
    ----------
    text : str
        Text.
    border : str
        Border text.

    Returns
    -------
    str
        Text.
    """

    return f'<table border="{border}">{text}</table>'

# --------------------------------------------------------------------------------------------------

def tr(text):
    """
    TR tag.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text.
    """

    return f'<tr>{text}</tr>'

# --------------------------------------------------------------------------------------------------

def th(text, width, valign='top'):
    """
    TH tag.

    Parameters
    ----------
    text : str
        Text.
    width : str
        Width text.
    valign : str
        Vertical align.

    Returns
    -------
    str
        Text.
    """

    if text == '':
        text = '&nbsp;'

    return f'<th width="{width}" valign="{valign}">{text}</th>'

# --------------------------------------------------------------------------------------------------

def td(text, valign='top'):
    """
    TD tag.

    Parameters
    ----------
    text : str
        Text.
    valign : str
        Valign text.

    Returns
    -------
    str
        Text.
    """

    if text == '':
        text = '&nbsp;'

    return f'<td valign="{valign}">{text}</td>'

# --------------------------------------------------------------------------------------------------

def h2(text):
    """
    H2 tag.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text.
    """

    return f'<h2>{text}</h2>'

# --------------------------------------------------------------------------------------------------

def font(text, color):
    """
    FONT tag.

    Parameters
    ----------
    text : str
        Text.
    color : str
        Color text.

    Returns
    -------
    str
        Text.
    """

    return f'<font color="{color}">{text}</font>'

# --------------------------------------------------------------------------------------------------

def center(text):
    """
    CENTER tag.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text.
    """

    return f'<center>{text}</center>'

# --------------------------------------------------------------------------------------------------

def b(text):
    """
    B tag.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text.
    """

    return f'<b>{text}</b>'
# --------------------------------------------------------------------------------------------------

def i(text):
    """
    I tag.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text.
    """

    return f'<i>{text}</i>'

# --------------------------------------------------------------------------------------------------

def ol(text):
    """
    OL tag.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text.
    """

    return f'<ol>{text}</ol>'

# --------------------------------------------------------------------------------------------------

def li(text):
    """
    LI tag.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text.
    """

    return f'<li>{text}</li>'

# ==================================================================================================
