contar(_, [], 0).
contar(OC, [X|L], Cont) :-
    contar(OC, L, Cont1),
    (OC == X -> Cont is Cont1 + 1 ; Cont = Cont1).