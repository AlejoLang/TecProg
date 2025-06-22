profundidad([], 1).
profundidad([X|L], Profundidad) :-
    is_list(X),
    profundidad(X, ProfundidadX),
    profundidad(L, ProfundidadL),
    Profundidad is max(ProfundidadX + 1, ProfundidadL).
profundidad([X|L], Profundidad) :-
    \+ is_list(X),
    profundidad(L, Profundidad).