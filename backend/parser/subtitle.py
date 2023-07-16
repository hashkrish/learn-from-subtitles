import srt


def parse_subtitle_text(contents: str):
    try:
        subs = srt.parse(contents)
    except srt.SRTParseError:
        raise ValueError("Invalid subtitle file")
    return subs
