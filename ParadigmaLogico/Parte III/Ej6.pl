suma_lista([], [], []).
suma_lista([X|L], [Y|L2], [Z|ListaSuma]) :-
    Z is X + Y,
    suma_lista(L,L2, ListaSuma).