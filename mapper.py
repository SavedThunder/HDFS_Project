
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.rstrip()
        line = line.split()
        if line[0] != "#":
            line.append('1')
            line = line[0] + " " + line[1] + " " + line[2] + " " + "\n"
            sys.stdout.write(line)
    
            
