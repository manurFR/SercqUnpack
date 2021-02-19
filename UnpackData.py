
DATAFILE = "../SERCQ/DATA.BIN"
CONVFILE = "../SERCQ/{0}"

SIZE_LINE = 34

OFFSET_EVENTS = 7 + 16
SIZE_EVENTS = 8

OFFSET_STRINGS_LOC =    7 + 0
OFFSET_PORTRAITS_LOC =  7 + 2
OFFSET_CHARA_LOC =      7 + 4
OFFSET_CHARANAME_LOC =  7 + 6
OFFSET_MAP_LOC =        7 + 8

TYPES = {1: "EVT_CONVERSATION", 2: "EVT_OBJECT", 3: "EVT_DESCRIPTION", 4: "EVT_ACTION"}
KEY = {"EVT_CONVERSATION": 'I', "EVT_OBJECT": 'F', "EVT_DESCRIPTION": 'R', "EVT_ACTION": 'A'}
ACTIONS = {1: "Voir le prisonnier#(vivant)",
           2: "Voir le prisonnier#(mort)",
           3: "Fantôme",
           4: "Répondre au téléphone",
           5: "Etac",
           6: "Passer le garde#(à Bréchou)",
           7: "Ouvrir le coffre",
           8: "Trésor",
           9: "Au moulin",
           10: "Bips à la station#hertzienne"}

ACCENTS = {'{': 'é', '}': 'è', '@': 'à', '~': 'ê', '|': 'ù'}

events = []


def timecode2time(timecode):
    hour = int(timecode / 8)
    minute = 8 * (timecode - (hour * 8))
    return "{0}H{1:02d}".format(hour, minute)


def calc_offset(offset_loc):
    # l'offset d'une section est lui-même à lire dans certains octets du fichiers (par groupe de 2 octets)
    return (fulldata[offset_loc + 1] << 8) + fulldata[offset_loc]


def convert_accents(achar):
    if achar in ACCENTS.keys():
        return ACCENTS[achar]
    else:
        return achar


def fetch_string(offset):
    result = []
    fetch_offset = offset
    while True:
        charval = fulldata[fetch_offset]
        if charval < 0x80:
            result.append(convert_accents(chr(charval)))
        else:
            result.append(convert_accents(chr(charval & 0x7f)))
            return ''.join(result), fetch_offset
        fetch_offset += 1


def print_detail(evt_type, evt_detail):
    key = KEY[evt_type]

    lines = []
    currline = []
    for idx, c in enumerate(evt_detail):
        if c != '#':
            currline.append(c)
        if c == '#' or len(currline) == SIZE_LINE:
            lines.append(currline)
            currline = []
    if currline:
        lines.append(currline)

    for idx, line in enumerate(lines):
        if idx == 0:
            margin = "  [{0}]   ".format(key)
        else:
            margin = ' ' * 8
        print("{0}{1}".format(margin, ''.join(line)))


with open(DATAFILE, 'rb') as fp:
    fulldata = [b for b in fp.read()]

offset_strings = calc_offset(OFFSET_STRINGS_LOC) + 7
offset_portraits = calc_offset(OFFSET_PORTRAITS_LOC) + 7
offset_chara = calc_offset(OFFSET_CHARA_LOC) + 7
offset_charaname = calc_offset(OFFSET_CHARANAME_LOC) + 7

# Parsing the "Events"
curr_offset = OFFSET_EVENTS
while True:
    event = fulldata[curr_offset:curr_offset+SIZE_EVENTS]
    if event[0] == 0:
        break
    type_event = TYPES[event[0] & 0xF]
    if type_event in ("EVT_OBJECT", "EVT_DESCRIPTION"):
        offset_event_loc = curr_offset + 6
        event_detail = calc_offset(offset_event_loc) + offset_strings
    elif type_event == "EVT_CONVERSATION":
        event_detail = "TEM0{0:02d}.TXT".format(event[6])
    else:  # EVT_ACTION
        event_detail = event[6]

    # print(event, type_event, event_detail)

    if event[5] < 0x23 and type_event != "EVT_ACTION":
        name_offset = calc_offset(offset_chara + event[5] * 3)
        name, _ = fetch_string(offset_charaname + name_offset)
        name = "{0} ({1})".format(name, event[5])
    else:
        name = str(event[5])

    # events : (x, y, start, end, charaId, type, stringOffset)
    events.append((event[1], event[2], timecode2time(event[3]), timecode2time(event[4]),
                   name, type_event, event_detail))
    curr_offset += SIZE_EVENTS

# Parsing the strings
curr_offset = offset_strings
strings = {}
while curr_offset < offset_portraits:
    parsed_string, end_offset = fetch_string(curr_offset)
    strings[curr_offset] = parsed_string
    curr_offset = end_offset + 1

# pprint(strings)

# Displaying each event with its detail
for evt in events:
    # if evt[0] == 136 and evt[1] == 137:
    print("event: x={0:3d} y={1:3d} start={2} end={3} charaId={4} type={5}".format(*evt))
    if evt[5] in ("EVT_OBJECT", "EVT_DESCRIPTION") and evt[6] in strings:
        print_detail(evt[5], strings[evt[6]])
    elif evt[5] == "EVT_CONVERSATION":
        with open(CONVFILE.format(evt[6]), 'r') as fp:
            conversation = fp.readlines()[0]

        end_conv = conversation.index(chr(0), 5)
        conversation = ''.join(convert_accents(c) for c in conversation[5:end_conv])

        print_detail(evt[5], conversation)
    else:  # EVT_ACTION
        print_detail(evt[5], "Action n°{0} [{1}]".format(str(evt[6]), ACTIONS[evt[6]]))
