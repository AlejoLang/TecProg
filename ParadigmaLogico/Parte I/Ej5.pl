ruta(santafe, parana).
ruta(parana, corrientes).
ruta(santafe, cordoba).
ruta(santafe, coronda).
ruta(santafe, rosario).
ruta(rosario, capital).
ruta(rosario, mardelplata).
ruta(capital, cordoba).

llega(Origen, Destino) :- 
    ruta(Origen, Destino).
llega(Origen, Destino) :-
    ruta(Origen, X),
    llega(X, Destino).
