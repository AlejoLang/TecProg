cantidad([], 0).
cantidad([_|L], Cont) :-
    cantidad(L, ContAux),
    Cont is ContAux + 1.
