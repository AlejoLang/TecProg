#lang racket

(define (full-reverse-list-map l)
    (reverse (map (lambda (x)
                     (if (list? x)
                         (full-reverse-list-map x) ; Aplica recursión si es una sublista
                         x)) ; Deja los elementos no lista como están
                   l))) ; Aplica map a la lista principal y luego la invierte

(full-reverse-list-map '(1 2 3 (4 5) (6 (7 8)) 9))