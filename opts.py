import argparse


def parse_opts():
    parser = argparse.ArgumentParser()
    # Datasets 
    parser.add_argument(
        '--videos',
        default='videos/',
        type=str,
        help='path of video files')
    
    args = parser.parse_args()

    return args
