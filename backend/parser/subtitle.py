import srt


def parse_subtitle_text(contents: str):
    try:
        subs = srt.parse(contents)
    except srt.SRTParseError:
        raise ValueError("Invalid subtitle file")
    return subs


if __name__ == "__main__":
    import sys
    import json

    merge_multi_lines = lambda x: x.replace("\n", " ")
    is_merge_multi_lines = len(sys.argv) > 2 and sys.argv[2] == "--merge-multi-lines"

    with open(sys.argv[1], "r") as f:
        contents = f.read()
    print(
        json.dumps(
            [
                {
                    "start": subtitle.start.total_seconds(),
                    "end": subtitle.end.total_seconds(),
                    "content": (
                        merge_multi_lines(subtitle.content)
                        if is_merge_multi_lines
                        else subtitle.content
                    ),
                }
                for subtitle in parse_subtitle_text(contents)
            ]
        )
    )
