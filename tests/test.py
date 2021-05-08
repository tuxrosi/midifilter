import sys
sys.path.append(".")
from midifilter.musicxmlparser import parse


def test_return_type():
    input = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
<part id="P1">
    <measure>
        <note>
            <type>quarter</type>
        </note>
    </measure>
</part>
</score-partwise>
    """
    assert parse(input) == ["quarter"]

def test_return_multiple_types():
    input = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
<part id="P1">
    <measure>
        <note>
            <type>quarter</type>
        </note>
        <note>
            <type>32nd</type>
        </note>
    </measure>
</part>
</score-partwise>
    """
    assert parse(input) == ["quarter", "32nd"]
