suma([], 0).
suma([X|L], Sum ):-
   suma(L, SumAux),
   Sum is SumAux + X. 