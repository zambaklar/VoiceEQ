import subprocess
import sys

def eq(inputf, outputf):
    
    cmd = [
        'ffmpeg',
        '-i', inputf,
        '-af', 'compand=attacks=0.3:points=-80/-80|-30/-15|-10/-10|0/-10|20/-20',
        '-c:v', 'copy',
        '-strict', 'experimental',
        outputf
    ]
    
    result = subprocess.run(cmd, stderr=subprocess.PIPE, text=True)

    if "Stream map" in result.stderr and "matches no streams" in result.stderr:
        cmd.remove('-c:v')
        cmd.remove('copy')
        subprocess.run(cmd)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 eq.py <input_file> <output_file>")
        sys.exit(1)

    inputf = sys.argv[1]
    outputf = sys.argv[2]

    eq(inputf, outputf)