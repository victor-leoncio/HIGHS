NAME  NURSE_SCHED
OBJSENSE
 MIN

ROWS
 N  COST
 G  C1
 G  C2
 G  C3
 G  C4
 G  C5
 G  C6

COLUMNS
    MARKER          ‘MARKER’    ‘INTORG’      ← início variáveis inteiras :contentReference[oaicite:2]{index=2}
    x1    COST      1            C1           1
    x2    COST      1            C2           1
    x3    COST      1            C3           1
    x4    COST      1.5          C4           1
    x5    COST      2            C5           1
    x6    COST      1            C6           1
    MARKER          ‘MARKER’    ‘INTEND’      ← fim variáveis inteiras :contentReference[oaicite:3]{index=3}

RHS
    RHS1   C1      50    C2    60    C3    50    C4    40    C5    30    C6    20

BOUNDS
 LO BND    x1      0
 LO BND    x2      0
 LO BND    x3      0
 LO BND    x4      0
 LO BND    x5      0
 LO BND    x6      0

ENDATA
