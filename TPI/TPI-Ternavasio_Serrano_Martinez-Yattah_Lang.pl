ciudad("Córdoba Capital").
ciudad("Carlos Paz").
ciudad("Bialet Masse").
ciudad("Valle Hermoso").
ciudad("La Falda").
ciudad("Huerta Grande").
ciudad("La Cumbre").
ciudad("Capilla Del Monte").

viaje("Córdoba Capital", "Carlos Paz", 1500).
viaje("Carlos Paz", "Bialet Masse", 1500).
viaje("Bialet Masse", "Valle Hermoso", 1000).
viaje("Valle Hermoso", "La Falda", 1200).
viaje("La Falda", "Huerta Grande", 1000).
viaje("Huerta Grande", "La Cumbre", 1200).
viaje("La Cumbre", "Capilla Del Monte", 1600).

viaja(jorge, "Córdoba Capital", "La Falda").
viaja(adriana, "Valle Hermoso", "La Cumbre").
viaja(gabriela, "Carlos Paz", "Capilla Del Monte").
viaja(roberto, "Bialet Masse", "Huerta Grande").
viaja(jose, "Córdoba Capital", "Capilla Del Monte").

% En base a una localidad de inicio y fin, obtiene la lista de localdiades intermedias (incluyendo el inicio y final)
% Parada
obtenerListaLoc(LocInicio, LocFin, [LocInicio]) :-
    ciudad(LocInicio),
    ciudad(LocFin),
    LocInicio == LocFin.
% Pred. recursivo 
obtenerListaLoc(LocInicio, LocFin, [LocInicio|Lista]) :-
    ciudad(LocInicio),
    ciudad(LocFin),
    LocInicio \= LocFin,
    viaje(LocInicio, Aux, _),
    obtenerListaLoc(Aux, LocFin, Lista).

% Predicado que permite ver si un valor esta dentro de una lista

estaEnLista(X, []) :-
    false.

estaEnLista(Elem, [X|L]) :-
    Elem == X.

estaEnLista(Elem, [X|L]) :-
    Elem \= X,
    estaEnLista(Elem, L).

% Obtiene una lista de pares que corresponden a un tramo (viaje de una ciudad a la siguiente) en base a un camino entre dos localidades
generarTramos([_], []).
generarTramos([A, B | Resto], [[A, B] | Tramos]) :-
    generarTramos([B | Resto], Tramos).

% Evalua verdadero si el viaje de Persona pasa por el tramo Orig-Dest (Orig y Dest son localidades consecutivas)
usaTramo(Persona, [Orig, Dest]) :-
    viaja(Persona, O, D),
    obtenerListaLoc(O, D, Camino),
    generarTramos(Camino, Tramos),
    estaEnLista([Orig, Dest], Tramos).


contar_usuarios(_, [], 0).
contar_usuarios(Tramo, [Persona | Resto], Cantidad) :-
    usaTramo(Persona, Tramo),
    contar_usuarios(Tramo, Resto, CantResto),
    Cantidad is CantResto + 1.
contar_usuarios(Tramo, [ _| Resto], Cantidad) :-
    contar_usuarios(Tramo, Resto, Cantidad).

% Calcular el costo total para una persona
costo_total(_, [], _, 0).
costo_total(Persona, [[Orig, Dest] | Tramos], Todas, Total) :-
    viaje(Orig, Dest, CostoTramo),
    contar_usuarios([Orig, Dest], Todas, Cant),
    costo_total(Persona, Tramos, Todas, TotalResto),
    Div is CostoTramo // Cant,
    Total is TotalResto + Div.

% Procesar una persona: [Nombre, Camino, CostoTotal]
procesar([], _, []).
procesar([Persona | Resto], Personas, [[Persona, Camino, Costo] | ResultadoResto]) :-
    viaja(Persona, Orig, Dest),
    obtenerListaLoc(Orig, Dest, Camino),
    generarTramos(Camino, Tramos),
    costo_total(Persona, Tramos, Personas, Costo),
    procesar(Resto, Personas, ResultadoResto).

% Predicado principal
repartir_costos(Personas, Resultado) :-
    procesar(Personas, Personas, Resultado).

tramosListaLoc([A|[B|Resto]],[(A,B)|Tramos]) :-
    tramosListaLoc([B|Resto], Tramos).