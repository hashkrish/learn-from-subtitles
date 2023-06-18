import srt


def parse_subtitle_text(contents: str):
    subs = srt.parse(contents)
    return subs
