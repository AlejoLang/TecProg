padre(leoncio, alberto).
padre(leoncio, geronimo).
padre(alberto, juan).
padre(alberto, luis).
padre(geronimo, luisa).

hermano(A, B) :- padre(P, A), padre(P, B), A \= B.
nieto(A, B) :- padre(B, P), padre(P, A).
