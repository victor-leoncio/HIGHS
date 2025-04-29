NAME          Enfermeiros
ROWS
 N  COST
 G  TURNO1
 G  TURNO2
 G  TURNO3
 G  TURNO4
 G  TURNO5
 G  TURNO6
COLUMNS
    X1       COST        1   TURNO1      1
    X1       TURNO2      1
    X2       COST        1   TURNO2      1
    X2       TURNO3      1
    X3       COST        1   TURNO3      1
    X3       TURNO4      1
    X4       COST        1.5 TURNO4      1
    X4       TURNO5      1
    X5       COST        2   TURNO5      1
    X6       COST        1   TURNO1      1
    X6       TURNO6      1
RHS
    RHS1    TURNO1      50
    RHS1    TURNO2      60
    RHS1    TURNO3      50
    RHS1    TURNO4      40
    RHS1    TURNO5      30
    RHS1    TURNO6      20
BOUNDS
 LO BND1      X1         0
 LO BND1      X2         0
 LO BND1      X3         0
 LO BND1      X4         0
 LO BND1      X5         0
 LO BND1      X6         20
ENDATA