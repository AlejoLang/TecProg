#lang racket

(define (agrupar l)
    (define (extraer l p (aux '()))
        (if (null? l)
            aux
            (if (equal? (car l) p)
                (extraer (cdr l) p (append aux (list (car l))))
                (extraer (cdr l) p aux))
        )
    )
    (if (null? l)
        '()
        (cons (extraer l (car l)) (agrupar (filter (lambda (x) (not (equal? x (car l)))) l)))
    )
)

(agrupar '(A A B C A B A D C)) ; Ejemplo de prueba