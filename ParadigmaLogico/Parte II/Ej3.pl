:- discontiguous gusta/2.

libro(rayuela, novela, larga).
libro(karamazov, novela, larga).
libro(octaedro, cuentos, corta).
libro(inventario, poemas, corta).
libro(leones, novela, corta).

mujer(haydée).
mujer(tanya).
hombre(livio).
hombre(pedro).

gusta(livio, rayuela).
gusta(pedro, inventario).
gusta(livio, inventario).

profesion(haydée, abogado).
profesion(haydée, ingeniero).
profesion(tanya, medico).
profesion(livio, contador).
profesion(pedro, abogado).

gusta(Persona, Libro) :-
    profesion(Persona, abogado),
    libro(Libro, novela, larga).

gusta(Persona, Libro) :-
    (profesion(Persona, ingeniero);profesion(Persona, medico)),
    libro(Libro, novela, _).

gusta(Persona, Libro) :-
    mujer(Persona),
    libro(Libro, _, larga).

gusta(Persona, Libro) :-
    hombre(Persona),
    profesion(Persona, contador),
    (libro(Libro, cuentos, _);libro(Libro, poemas, _)).


libroValioso(Libro) :-
    gusta(X, Libro), 
    gusta(Y, Libro),
    X \= Y.