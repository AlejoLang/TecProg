entrada(ensalada).
entrada(papas).
entrada(tarta).
plato_principal('lomo a la pimienta').
plato_principal(locro).
plato_principal(asado).
postre(flan).
postre(helado).
postre(alfajor).

carta(X, Y, Z) :- entrada(X), plato_principal(Y), postre(Z).

mostrar_carta(X, Y, Z) :-
    carta(X, Y, Z),
    format('entrada = ~w, plato principal = ~w, postre = ~w~n', [X, Y, Z]),
    fail.

