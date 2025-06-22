positivos([], []).
positivos([X|L], [X|ListaPositivos]) :-
    X > 0,
    positivos(L, ListaPositivos).
positivos([X|L], ListaPositivos) :-
    X =< 0,
    positivos(L, ListaPositivos).
