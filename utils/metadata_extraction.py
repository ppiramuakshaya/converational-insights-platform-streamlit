import ffmpeg

def extract_metadata(file_path):
    probe = ffmpeg.probe(file_path)
    return probe['streams'][0]

