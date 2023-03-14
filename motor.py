FORWARD = (1, 0)
BACKWARD = (0, 1)
RELEASE = (0, 0)

# format data for writing to shift register
# returns [4B, 3B, 4A, 2B, 1B, 1A, 2A, 3A]
def getBinaryList(stateList: list[tuple[int]]):
    if len(stateList) != 3:
        raise Exception("Input list must contain 3 states.")
    stateList.append(RELEASE)  # fourth motor is not used
    for state in stateList:
        if state not in (FORWARD, BACKWARD, RELEASE):
            raise Exception("Invalid state in input list.")
    motorValues = [val for state in stateList for val in state]  # convert to flat list
    # see shield schematic (http://wiki.sunfounder.cc/images/f/ff/L293D_schematic.png)
    shieldConfig = (4, 2, 0, 1, 3, 6, 5, 7)
    motorData = [motorValues[i] for i in shieldConfig]
    motorData.reverse()  # reverse since while writing, first value becomes LSB
    return motorData


SampleStates = [
    [RELEASE, RELEASE, RELEASE],
    [FORWARD, RELEASE, RELEASE],
    [RELEASE, FORWARD, RELEASE],
    [RELEASE, RELEASE, FORWARD],
    [RELEASE, RELEASE, RELEASE],
    [BACKWARD, RELEASE, RELEASE],
    [RELEASE, BACKWARD, RELEASE],
    [RELEASE, RELEASE, BACKWARD],
    [RELEASE, RELEASE, RELEASE],
    [FORWARD, FORWARD, RELEASE],
    [RELEASE, FORWARD, FORWARD],
    [FORWARD, RELEASE, FORWARD],
    [RELEASE, RELEASE, RELEASE],
    [BACKWARD, BACKWARD, RELEASE],
    [RELEASE, BACKWARD, BACKWARD],
    [BACKWARD, RELEASE, BACKWARD],
    [RELEASE, RELEASE, RELEASE],
    [FORWARD, FORWARD, FORWARD],
    [RELEASE, RELEASE, RELEASE],
    [BACKWARD, BACKWARD, BACKWARD],
    [RELEASE, RELEASE, RELEASE],
]
