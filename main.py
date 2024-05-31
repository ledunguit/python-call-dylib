import ctypes
import sys

def call_hashes(algo, input_filename, output_filename):
    lib.calculate_hashes(algo, input_filename, output_filename)

if __name__ == '__main__':
    # check number of arguments
    if len(sys.argv) != 4:
        print('Usage: python main.py <algorithm> <input_file> <output_file>')
        sys.exit(1)

    lib = ctypes.CDLL('./libhashdll.dylib')

    lib.calculate_hashes.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
    lib.calculate_hashes.restype = None

    # load from arguments and convert to UTF-8
    algo = sys.argv[1].encode('utf-8')
    input_filename = sys.argv[2].encode('utf-8')
    output_filename = sys.argv[3].encode('utf-8')

    call_hashes(algo, input_filename, output_filename)