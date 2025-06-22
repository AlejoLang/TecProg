eliminar_dup([], []).
eliminar_dup([X|L], [X|SinDup]) :-
    eliminar_dup(L, SinDup),
    not(member(X, L)).
eliminar_dup([X|L], SinDup) :-
    eliminar_dup(L, SinDup),
    member(X, L).
