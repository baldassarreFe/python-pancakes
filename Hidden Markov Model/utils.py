from bisect import bisect_left
import sys

# Displays or updates a console progress bar
# Thanks to http://stackoverflow.com/a/15860757/3526592
## Accepts a float between 0 and 1. Any int will be converted to a float.
## A value under 0 represents a 'halt'.
## A value at 1 or bigger represents 100%
def updateProgress(progress):
    barLength = 50
    status = ""
    fullBlock = "#"
    emptyBlock = "-"
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    blocks = int(round(barLength*progress))
    text = "\r[{0}] {1:.3f}% {2}".format(fullBlock*blocks + emptyBlock*(barLength-blocks), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()

def binarySearch(arr, x):
    pos = bisect_left(arr,x) # find insertion position
    return pos if pos != len(arr) and arr[pos] == x else -1 # don't walk off the end

if __name__ == '__main__':
    import time
    for t in range(101):
        time.sleep(0.05)
        updateProgress(t/100)

    a = [3, 4, 6, 7]
    print("a =",a)
    print("Searching 4:", binarySearch(a, 4))
    print("Searching 5:", binarySearch(a, 5))
    print("Searching 1:", binarySearch(a, 1))
    print("Searching 9:", binarySearch(a, 9))

    a = "ABCE"
    print("a =",a)
    print("Searching B", binarySearch(a,"B"))
