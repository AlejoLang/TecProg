#lang racket

(define (pesopalabra p)
    (if (null? p)
        0
        (+ (char->integer (car p)) (pesopalabra (cdr p)))
    ) 
)

(define (obtener-menor-peso x (m (car x)))
    (if (null? x)
        m
        (if (< (pesopalabra (string->list (car x))) (pesopalabra (string->list )))
            (obtener-menor-peso (cdr x) (car x))
            (obtener-menor-peso (cdr x) m)
        )
    )
)

(define (eliminar-ocurrencia l x)
    (if (null? l)
        '()
        (if (string=? (car l) x)
            (cdr l)
            (cons (car l) (eliminar-ocurrencia (cdr l) x))
        )
    )
)

(define (ordenar l)
    (if (null? l)
        '()
        (cons (obtener-menor-peso l) (ordenar (eliminar-ocurrencia l (obtener-menor-peso l))))
    )
)

(ordenar '( "moto" "auto" "casa" "juego" "aire"))
(ordenar '("d" "c" "b" "a"))
(ordenar '("asdklasjf" "askldja" "lkdsajflkasdf"))