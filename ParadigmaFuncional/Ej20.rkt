#lang racket

(define (full-reverse-list l)
    (if (null? l)
        '()
        (if (list? (car l))
            (append (full-reverse-list (cdr l)) (list (full-reverse-list (car l)))) 
            (append (full-reverse-list (cdr l)) (list (car l))) ; Usa append para concatenar correctamente
        )
    )
)

(full-reverse-list '(1 2 3 4 5 6 7 8 9 (1 2)))
(full-reverse-list '((1 2) 3 4 (5 (6 7 (8 9)))))
(full-reverse-list '(1 (2 (3 (4 (5 (6 (7 (8 (9))))))))))