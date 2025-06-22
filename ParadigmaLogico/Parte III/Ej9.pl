insertar(Elem, [], []).
insertar(Elem, [X|L], [Elem|Resultado]) :-
    X @=< Elem,
    L = [Y, _],
    Y @>= Elem, 
    insertar(Elem, L, Resultado).
insertar(Elem, [X|L], [X|Resultado]) :-
    insertar(Elem, L, Resultado).