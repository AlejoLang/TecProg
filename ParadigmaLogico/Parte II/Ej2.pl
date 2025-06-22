hombre(juan).
hombre(luis).
hombre(alberto).
mujer(lara).
mujer(juana).
mujer(maria).
mujer(carla).

progenitor(juan, luis).
progenitor(juan, alberto).
progenitor(alberto, lara).
progenitor(alberto, carla).
progenitor(lara, juana).
progenitor(juana, maria).

padre(X, Y) :- hombre(X), progenitor(X, Y).
madre(X, Y) :- mujer(X), progenitor(X, Y).
abuelo(X, Y) :- hombre(X), progenitor(X, Z), progenitor(Z, Y).
abuela(X, Y) :- mujer(X), progenitor(X, Z), progenitor(Z, Y).
hermano(X, Y) :- hombre(X), progenitor(Z, X), progenitor(Z, Y), X \= Y.
hermana(X, Y) :- mujer(X), progenitor(Z, X), progenitor(Z, Y), X \= Y.

sucesor(X, Y) :- progenitor(Y, X), !.
sucesor(X, Y) :-
    progenitor(Z, X),sucesor(Z, Y).

es_madre(X) :-
    mujer(X), progenitor(X, Y).
es_padre(X) :-
    hombre(X), progenitor(X, Y).

tia(X, Y) :-
    mujer(X),
    progenitor(Z, Y),
    (hermana(X, Z) ; hermano(X, Z)), !.

