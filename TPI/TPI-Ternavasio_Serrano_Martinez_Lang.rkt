#lang racket

(struct localidad (nombre precioProx horarios))
(struct horaminutos (hora minuto))


; Retorna verdadero si x >= y y falso si x < y
(define (comparar-hora x y)
    (let ((xHoraNum (horaminutos-hora x))
          (xMinNum (horaminutos-minuto x))
          (yHoraNum (horaminutos-hora y))
          (yMinNum (horaminutos-minuto y))
          )
        (if (> xHoraNum yHoraNum)
            #t
            (if (eq? xHoraNum yHoraNum)
                (if (< xMinNum yMinNum)
                    #f
                    #t 
                ) 
                #f
            )
        )
    )    
)

(define data 
    (list 
        (localidad "Córdoba Capital" 1500 (list (horaminutos 07 00) (horaminutos 10 00) (horaminutos 12 00)))
        (localidad "Carlos Paz" 1500 (list (horaminutos 07 30) (horaminutos 10 30) (horaminutos 12 30)))
        (localidad "Bialet Massé" 1000 (list (horaminutos 07 45) (horaminutos 10 45) (horaminutos 12 45)))
        (localidad "Valle Hermoso" 1200 (list (horaminutos 08 15) (horaminutos 11 15) (horaminutos 13 15)))
        (localidad "La Falda" 1000 (list (horaminutos 08 30) (horaminutos 11 30) (horaminutos 13 30)))
        (localidad "Huerta Grande" 1200 (list (horaminutos 08 45) (horaminutos 11 45) (horaminutos 13 45)))
        (localidad "La Cumbre" 1600 (list (horaminutos 09 30) (horaminutos 12 30) (horaminutos 14 30)))
        (localidad "Capilla Del Monte" 0 (list (horaminutos 10 00) (horaminutos 13 00) (horaminutos 15 00)))
    )
)

; Busca la lista de localidades desde el principio, si se encuentra el origen se retorna verdadero y si 
; se encuentra el destino retorna falso significando que el destino estaba antes del origen
; Si no se encuentra ninguno retorna tambien falso
(define (comprobarOrigenDestino origen destino (l data))
    (if (string=? origen destino)
        #f
        (if (null? l)
            #f
            (if (string=? (localidad-nombre (car l)) origen)
                #t
                (if (string=? (localidad-nombre (car l)) destino)
                    #f
                    (comprobarOrigenDestino origen destino (cdr l))
                )
            )
        )
    )
)

; Verifica si una localidad existe por su nombre
(define (verificarExistencia nombre (l data))
    (if (null? l)
        #f
        (if (string=? (localidad-nombre (car l)) nombre)
            #t
            (verificarExistencia nombre (cdr l))
        )
    )
)

; Retorna la lista de horarios para una cierta localidad
(define (horariosLocalidad nombre (l data))
    (if (null? data)
        null
        (if (string=? (localidad-nombre (car l)) nombre)
            (localidad-horarios (car l))
            (horariosLocalidad nombre (cdr l))
        )
    )
)

; Recibe una lista de horarios y un horario de referencia y retorna otra lista con los horarios que son mayores a la referencia
(define (horariosDisponibles locHor hor) 
    ; Crea una lista de horaminuto con los horarios superiores al argumento
    (if (null? locHor) 
        '()
        (if (comparar-hora (car locHor) hor)
            (cons (car locHor) (horariosDisponibles (cdr locHor) hor))
            (horariosDisponibles (cdr locHor) hor)
        )
    )
)

; Obtiene los precios entre un origen y un destino
; Se llama recursivamente recorriendo la lista hasta llegar al origen
; A partir de ahi, suma el costo de viaje a la proxima localidad mas el costo del resto del camino
; El costo del resto del camino se calcula recursivamente llamando a la funcion pero estableciendo el origen como el siguiente elemento luego de encontrar
; el verdadero origen, de esta forma se ahorra el volver a recorrer la lista entera nuevamente

(define (obtenerPrecios origen destino (locs data))
    (if (null? (cdr locs))
        0
        (if (and (string=? origen (localidad-nombre (car locs))) (not (string=? origen destino)))
            (+ (localidad-precioProx (car locs)) (obtenerPrecios (localidad-nombre (car (cdr locs))) destino (cdr locs))) 
            (if (string=? destino (localidad-nombre (car locs)))
                0
                (obtenerPrecios origen destino (cdr locs)) 
            )
        ) 
    )
)

; Recibe una lista de horaminuto y lo retorna en un formato ((hh mm) (hh mm))
(define (desestructHoraminutos x)
    (if (null? x) 
        '()
        (cons (list (~r (horaminutos-hora (car x)) #:min-width 2 #:pad-string "0")
                    (~r (horaminutos-minuto (car x)) #:min-width 2 #:pad-string "0"))
              (desestructHoraminutos (cdr x)))
    )
)

; Retora la planificación del viaje o errores en el caso de haberlos
; Primero verifica si el origen es una ciudad anterior al destino y luego si el destino existe, esto se hace
; porque, por como funciona comprobarOrigenDestino, si el origen es válido y el destino no, retornara verdadero 
; igualmente por lo que hay que considerar el caso extra

; Luego obtiene los horarios de la localidad origen y le aplica la función horariosDisponibles para obtener los horarios
; que son mayores al ingresado, si esa lista esta vacia significa que no hay horarios disponibles por lo que retorna el error
; Si la lista no esta vacia procede a formar la respuesta invocando a obtenerPrecios y el desestructurador de los horarios disponibles

(define (ArgentinaTur param)
    (if (and (eq? (length param) 3) (list? (caddr param)) (eq? (length (caddr param)) 2))
        (let ((origen (car param))
                (destino (cadr param))
                (horarioIng (horaminutos (caaddr param) (car (cdaddr param)))))
            (if (and (comprobarOrigenDestino origen destino) (verificarExistencia destino))
                (let ((horariosDisp (horariosDisponibles (horariosLocalidad origen) horarioIng)))
                    (if (null? horariosDisp)
                        (list (list origen destino) 0 "NO HAY HORARIOS DISPONIBLES")
                        (list (list origen destino) (obtenerPrecios origen destino) (desestructHoraminutos horariosDisp)) 
                    )
                )
                "ERROR"
            ) 
        )
        "ERROR"
    )
)
